axios.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access');
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

axios.interceptors.response.use(
    response => {
        return response;
    },
    async error => {
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            const refreshToken = localStorage.getItem("refresh");
            return axios.post("http://127.0.0.1:8000/api/account/refresh/", { refresh: refreshToken })
                .then(response => {
                    localStorage.setItem("access", response.data.access);
                    localStorage.setItem("refresh", response.data.refresh);
                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    originalRequest.headers["Authorization"] = "Bearer " + response.data.access;
                    return axios(originalRequest);
                })
                .catch(error => {
                    window.location.href = "/login/";
                    return Promise.reject(error);
                });
        }
        return Promise.reject(error);
    }
);