<div style ="text-align:center">

  # VITA-INFO

</div>



<p align='center'><strong>“사용자에게 맞춤형으로 영양제 정보를 제공해주는 웹 사이트”</strong></p>
</p>
  <ul>
  <li><strong>프로젝트 명: </strong><a href="https://vitainfo.kr"> VITA INFO</a></li>
  <li><strong>팀 명:</strong> VITA INFO</li>
  <li><strong>프로젝트 기간:</strong> 24.05.13 ~ 24.06.12</li>
  <li><strong>팀 원:</strong> 이정우, 이태훈, 김범중, 지효상</li>
</ul>
<br>


## 팀원 소개 및 역할
<table>
<thead>
<tr>
<th>이정우 <br>(팀장)</th>
<th>이태훈 <br>(부팀장)</th>
<th>김범중 <br>(팀원)</th>
<th>지효상 <br>(팀원)</th>
</tr>
</thead>
<tbody>
<tr>
  <td>
    <p align="center">
      서비스 시스템 설계<br>
      post app 구현<br>
      소프트웨어 형상 관리<br>
      일정 관리
    </p>
  </td>
    <td>
    <p align="center">
      서비스 시스템 설계<br>
      user app 구현<br>
      소프트웨어 형상 관리<br>
      일정 관리
    </p>
  </td>
  
  <td>
    <p align="center">
      서비스 시스템 설계<br>
      post app 구현<br>
    </p>
  </td>
  
  <td>
    <p align="center">
   서비스 시스템 설계<br>
  survey app 구현
    </p>
  </td>
</tr>
</tbody>
</table>

<br>

## 기술 스택
![기술스택](https://github.com/JWTONE/VITA-INFO/assets/159910835/30ce8301-35dc-45f7-a969-779d71485ce2)


## 시스템 아키텍처
![아키텍처](https://github.com/JWTONE/VITA-INFO/assets/159910835/f4047c1c-a83b-4d56-8933-542baa9e7aa5)


## 화면 요약(와이어 프레임)
![와이어프레임](https://github.com/JWTONE/VITA-INFO/assets/159910835/04fa97b7-1c8f-4561-a062-d29408c157f0)

## API명세 

<details>
  
<summary>
  
  ### 회원
  
</summary>

- **회원가입**
  - HTTP 메소드: POST
  - API Path: `/api/account/`


- **로그인**
  - HTTP 메소드: POST
  - API Path: `/api/account/login`

- **토큰 Refresh**
  - HTTP 메소드: POST
  - API Path: `/api/account/refresh`

- **로그아웃**
  - HTTP 메소드: POST
  - API Path: `/api/account/logout`

- **회원탈퇴**
  - HTTP 메소드: DELETE
  - API Path: `/api/account/`

- **회원정보 수정**
  - HTTP 메소드: PUT
  - API Path: `/api/account/<str:username>`

- **비밀번호 수정**
  - HTTP 메소드: PUT
  - API Path: `/api/account/<str:username>/password`

</details>

<details>
  
<summary>
  
  ### 게시글
  
</summary>

- **게시글 작성**
  - HTTP 메소드: GET
  - API Path: `/api/post/`

- **게시글 리스트 조회**
  - HTTP 메소드: GET
  - API Path: `/api/post/<str:category>`

- **게시글 검색**
  - HTTP 메소드: GET
  - API Path: `/api/post/search/`

- **게시글 상세 조회**
  - HTTP 메소드: GET
  - API Path: `/api/post/<int:post_pk>`

- **게시글 수정**
  - HTTP 메소드: PUT
  - API Path: `/api/post/<int:post_pk>`

- **게시글 삭제**
  - HTTP 메소드: DELETE
  - API Path: `/api/post/<int:post_pk>`

- **게시글 좋아요**
  - HTTP 메소드: POST
  - API Path: `/api/post/<int:post_pk>`

- **댓글 작성**
  - HTTP 메소드: POST
  - API Path: `/api/post/<int:post_pk>/comment/`

- **대댓글 작성**
  - HTTP 메소드: POST
  - API Path: `/api/post/<int:post_pk>/comment/<int:comment_pk>`

- **댓글 조회**
  - HTTP 메소드: GET
  - API Path: `/api/post/<int:post_pk>/comment/`

- **댓글 수정**
  - HTTP 메소드: PUT
  - API Path: `/api/post/comment/<int:comment_pk>`

- **댓글 좋아요**
  - HTTP 메소드: POST
  - API Path: `/api/post/comment/<int:comment_pk>`

- **인기 검색어 순위**
  - HTTP 메소드: GET
  - API Path: `/api/post/ranking/`
  - 
</details>

<details>
  
<summary>
  
  ### 설문조사
  
</summary>

- **설문 보내기**
  - HTTP 메소드: POST
  - API Path: `/api/survey/`

- **로딩페이지**
  - HTTP 메소드: GET
  - API Path: `/api/survey/loading/`

- **설문조사 결과 불러오기**
  - HTTP 메소드: GET
  - API Path: `/api/survey/`

</details>

## 상태 관리 tool 선택
**결과 및 회고**


### 트러블슈팅


## 협업 방식
### 매일 아침 회의마다 daily task 공유(figma 활용)
![피그마_1](https://github.com/JWTONE/VITA-INFO/assets/159910835/f19a0f99-defe-457a-9601-c28d4ff6fdd5)
![피그마_2](https://github.com/JWTONE/VITA-INFO/assets/159910835/728e3e29-d78a-4960-81c2-d24a7d107556)
