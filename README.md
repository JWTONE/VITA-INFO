<div style ="text-align:center">

  # VITA-INFO

</div>



<p align='center'><strong>“사용자에게 맞춤형으로 영양제 정보를 제공해주는 웹 사이트”</strong></p>
</p>
  <ul>
  <li><strong>프로젝트 명: </strong><a href="https://vitainfo.kr"> VITA INFO</a></li>
  <li><strong>팀 명:</strong> VITA INFO</li>
  <li><strong>프로젝트 기간:</strong> 24.05.13 ~ 24.06.13</li>
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
  - HTTP Method: POST
  - API Path: `/api/account/`
  - Request:
    ```json
    {
        "username": "string",
        "password": "string",
        "confirm_password": "string",
        "email": "email",
        "name": "string",
        "nickname": "string",
        "date_of_birth": "date",
        "gender": "string",
        "subscription": "boolean"
    }
    ```
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 



- **로그인**
  - HTTP Method: POST
  - API Path: `/api/account/login`
  - Request:
    ```json
    {
        "username": "string",
        "password": "string",
    }
    ```
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **토큰 Refresh**
  - HTTP Method: POST
  - API Path: `/api/account/refresh`
  - Request:
    ```json
    {
        "refresh" : "string"
    }
    ```
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 401


- **로그아웃**
  - HTTP Method: POST
  - API Path: `/api/account/logout`
  - Request:
    ```json
    {
        "refresh" : "string"
    }
    ```
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **회원탈퇴**
  - HTTP Method: DELETE
  - API Path: `/api/account/`
  - Request:
    ```json
    {
        "password": "string",
    }
    ```
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **회원정보 수정**
  - HTTP Method: PUT
  - API Path: `/api/account/<str:username>`
  - Request:
    ```json
    {
        "email": "email",
        "date_of_birth": "date",
        "gender": "string",
        "subscription": "boolean"
    }
    ```
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **비밀번호 수정**
  - HTTP Method: PUT
  - API Path: `/api/account/<str:username>/password`
  - Request:
    ```json
    {
        "password": "string",
        "confirm_password": "string",
    }
    ```
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


</details>

<details>
  
<summary>
  
  ### 게시글
  
</summary>

- **게시글 작성**
  - HTTP Method: POST
  - API Path: `/api/post/`
  - Request:
    ```json
    {
        "title":"string",
        "content":"string"
    }
    ```
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **게시글 리스트 조회**
  - HTTP Method: GET
  - API Path: `/api/post/<str:category>`
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **게시글 검색**
  - HTTP Method: GET
  - API Path: `/api/post/search/`
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **게시글 상세 조회**
  - HTTP Method: GET
  - API Path: `/api/post/<int:post_pk>`
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **게시글 수정**
  - HTTP Method: PUT
  - API Path: `/api/post/<int:post_pk>`
  - Request:
    ```json
    {
        "title":"string",
        "content":"string"
    }
    ```
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **게시글 삭제**
  - HTTP Method: DELETE
  - API Path: `/api/post/<int:post_pk>`
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **게시글 좋아요**
  - HTTP Method: POST
  - API Path: `/api/post/<int:post_pk>`
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **댓글 작성**
  - HTTP Method: POST
  - API Path: `/api/post/<int:post_pk>/comment/`
  - Request:
    ```json
    {
        "content":"string"
    }
    ```
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **대댓글 작성**
  - HTTP Method: POST
  - API Path: `/api/post/<int:post_pk>/comment/<int:comment_pk>`
  - Request:
    ```json
    {
        "title":"string",
        "content":"string"
    }
    ```
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **댓글 조회**
  - HTTP Method: GET
  - API Path: `/api/post/<int:post_pk>/comment/`
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **댓글 수정**
  - HTTP Method: PUT
  - API Path: `/api/post/comment/<int:comment_pk>`
  - Request:
    ```json
    {
        "title":"string",
        "content":"string"
    }
    ```
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **댓글 좋아요**
  - HTTP Method: POST
  - API Path: `/api/post/comment/<int:comment_pk>`
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **인기 검색어 순위**
  - HTTP Method: GET
  - API Path: `/api/post/ranking/`
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 

  - 
</details>

<details>
  
<summary>
  
  ### 설문조사
  
</summary>

- **설문 보내기**
  - HTTP Method: POST
  - API Path: `/api/survey/`
  - Request:
    ```json
    {
        "name":"string",
        "gender":"string",
        "age":"integer",
        "height":"integer",
        "weight":"integer",
        "current_medications_or_supplements":"string",
        "allergies":"string",
        "exercise_frequency_per_week":"string",
        "average_sleep_hours_per_day":"string",
        "smoking_status":"string",
        "alcohol_consumption":"string",
        "average_meals_per_day":"string",
        "main_foods" : "string",
        "snacks" : "string",
        "health_goals": "string",
        "interested_supplements" : "string",
        "specific_health_issues_to_improve" : "string"
    }
    ```
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **로딩페이지**
  - HTTP Method: GET
  - API Path: `/api/survey/loading/`
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


- **설문조사 결과 불러오기**
  - HTTP Method: GET
  - API Path: `/api/survey/`
  - Response:
    
    &emsp;&emsp; 성공, 200

    &emsp;&emsp; 실패, 400 


</details>

## 상태 관리 tool 선택
**결과 및 회고**


### 트러블슈팅


## 협업 방식
### 매일 아침 회의마다 daily task 공유(figma 활용)
![피그마_1](https://github.com/JWTONE/VITA-INFO/assets/159910835/f19a0f99-defe-457a-9601-c28d4ff6fdd5)
![피그마_2](https://github.com/JWTONE/VITA-INFO/assets/159910835/728e3e29-d78a-4960-81c2-d24a7d107556)
