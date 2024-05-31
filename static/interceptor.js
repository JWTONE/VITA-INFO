axios.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access');
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        Promise.reject(error);
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
            const refreshToken = localStorage.getItem("refresh_token");
            return axios.post("api/account/refresh/", { refresh: refreshToken })
                .then(response => {
                    localStorage.setItem("access_token", response.data.access);
                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    originalRequest.headers["Authorization"] = "Bearer " + response.data.access;
                    return axios(originalRequest);
                })
                .catch(err => {
                    console.error("리프레시 토큰 갱신 실패:", err);
                    localStorage.removeItem("access_token");
                    localStorage.removeItem("refresh_token");
                    window.location.href = "/";
                    return Promise.reject(error);
                });
        }
        return Promise.reject(error);
    }
);