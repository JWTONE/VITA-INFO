import axios from 'axios';

// 로그인 함수
async function login(username, password) {
    try {
        const response = await axios.post('http://127.0.0.1:8000/api/account/login/', {
            username: username,
            password: password
        });
        const { access, refresh } = response.data;

        // 토큰을 로컬 스토리지에 저장
        localStorage.setItem('access_token', access);
        localStorage.setItem('refresh_token', refresh);

        // Axios 기본 설정에 토큰 추가
        axios.defaults.headers.common['Authorization'] = `Bearer ${access}`;
        
        return true;
    } catch (error) {
        console.error('로그인 실패:', error);
        return false;
    }
}

// 로그아웃 함수
async function logout() {
    try {
        const refresh_token = localStorage.getItem('refresh_token');

        await axios.post('http://127.0.0.1:8000/api/account/logout/', {
            refresh: refresh_token
        });

        // 토큰 삭제
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');

        delete axios.defaults.headers.common['Authorization'];
        
        return true;
    } catch (error) {
        console.error('로그아웃 실패:', error);
        return false;
    }
}

// 토큰 갱신 함수
async function refreshToken() {
    try {
        const refresh_token = localStorage.getItem('refresh_token');

        const response = await axios.post('http://127.0.0.1:8000/api/account/refresh/', {
            refresh: refresh_token
        });

        const { access } = response.data;

        // 새로운 액세스 토큰 저장
        localStorage.setItem('access_token', access);

        // Axios 기본 설정에 새로운 토큰 추가
        axios.defaults.headers.common['Authorization'] = `Bearer ${access}`;
        
        return true;
    } catch (error) {
        console.error('토큰 갱신 실패:', error);
        return false;
    }
}

export { login, logout, refreshToken };
