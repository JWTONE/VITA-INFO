import { login, logout } from './login';

// 로그인 버튼 클릭 시
document.getElementById('login-button').addEventListener('click', async () => {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const success = await login(username, password);
    if (success) {
        console.log('로그인 성공');
    } else {
        console.log('로그인 실패');
    }
});

// 로그아웃 버튼 클릭 시
document.getElementById('logout-button').addEventListener('click', async () => {
    const success = await logout();
    if (success) {
        console.log('로그아웃 성공');
    } else {
        console.log('로그아웃 실패');
    }
});
