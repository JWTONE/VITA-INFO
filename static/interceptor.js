axios.interceptors.request.use(
    (config) => {
        // 만약 로그아웃 요청이면 Authorization 헤더를 삭제
        if (config.url === "http://127.0.0.1:8000/api/account/logout/") {
            delete config.headers.Authorization;
        } else {
            const token = localStorage.getItem('access');
            if (token) {
                config.headers['Authorization'] = `Bearer ${token}`;
            }
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
    error => {
        const originalRequest = error.config;

        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            const refreshToken = localStorage.getItem("refresh");

            if (refreshToken) {
                axios.post("http://127.0.0.1:8000/api/account/refresh/", { refresh: refreshToken })
                    .then(response => {
                        localStorage.setItem("access", response.data.access);
                        localStorage.setItem("refresh", response.data.refresh);
                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                        originalRequest.headers["Authorization"] = "Bearer " + response.data.access;
                        return axios(originalRequest);
                    })
                    .catch(refreshError => {
                        // Refresh Token이 만료되었으므로 로그인 페이지로 이동
                        window.localStorage.clear();
                        window.location.href = "/login/";
                        // refreshError를 처리하고 에러를 전달
                        throw refreshError;
                    });
            } else {
                localStorage.removeItem("access");
                localStorage.removeItem("refresh");
                window.location.href = "/login/";
                // 에러를 전달
                throw error;
            }
        }

        // 요청이 실패한 경우 에러를 전달
        return Promise.reject(error);
    }
);
