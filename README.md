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
      일정 관리 <br>
      프론트엔드 적용
    </p>
  </td>
    <td>
    <p align="center">
      서비스 시스템 설계<br>
      user app 구현<br>
      소프트웨어 형상 관리<br>
      일정 관리 <br>
      로그인 관련 axios 적용<br>
      WYSIWYG 적용
    </p>
  </td>
  
  <td>
    <p align="center">
      서비스 시스템 설계<br>
      post app 구현<br>
      로그인 관련 axios 적용<br>
      Redis 이용한 실시간 인기 검색어
    </p>
  </td>
  
  <td>
    <p align="center">
   서비스 시스템 설계<br>
  survey app 구현<br>
  aws 배포 환경 구축<br>
  https 프로토콜 적용
    </p>
  </td>
</tr>
</tbody>
</table>

<br>

## 기술 스택
![기술스택](![alt text](image.png))


## 시스템 아키텍처
![아키텍처](https://github.com/JWTONE/VITA-INFO/assets/159910835/f4047c1c-a83b-4d56-8933-542baa9e7aa5)
![아키텍처](https://cdn.discordapp.com/attachments/1232611383309238339/1250654517855522826/image.png?ex=666bba49&is=666a68c9&hm=726b6b71e76fd03a1f9d52aa7d1e1b785ebc85bef4fb94ea416a4f46356e6621&)


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


<hr>

<details>

<summary>

  ### 트러블슈팅

</summary>

<details>

  <summary>
    
  ### ChatGPT 결과 정형화 되지 않은 문제
  
  </summary>
 
  
  #### 문제

  설문조사 결과를 화면에 출력시켜주고 데이터베이스에 저장 해야 하는데 답변의 형식이 매번 다르게 출력되어 작동하지 않는 문제 발생

  #### 해결

  정형화된 답변 틀을 제공해주고, 이 데이터들을 쉽게 다루기 위해서 python dictionary 형식으로 출력 해주도록  쿼리문을 변경했습니다.

</details>

  <details>

  <summary>
    
  ### ChatGPT 가 말도 안되는 결과를 출력
  
</summary>
  
  #### 문제

  설문 내용에 대한 답변에, 아마씨를  ‘아마겟돈’으로 잘못 알려주는 현상 발생 

  #### 해결

  다 방면으로 노력해봤지만, 이미 학습한 내용은 바꿔주기가 어려워서 GPT4.0Turbo로 모델로 변경 적용 해보니, 아마씨도 정상적으로 출력함

</details>

<details>

<summary>
    
  ### Axios interceptor 작동 안함
  
</summary>
  
  #### 문제

  로그인후 request 보냈을  access token이 안불러와지는 문제가 발생

  #### 해결

  로직에는 문제가 없었지만, base를 상속받는 template에서 axios 관련 cdn을 다시 불러와 서 충돌이 발생, 템플릿에서 cdn을 제외 하니 interceptor정상 작동

</details>

<details>

<summary>
  
  ### 댓글 출력 문제

</summary>


  #### 문제

  댓글 작성 시 대댓글들이 부모 댓글 및으로 상속 되지 않고 pk 순서 대로 출력 되는 문제 발생

  #### 해결

  시리얼라이저에 is_reply라는 필드를 추가해서 is_reply일 경우에 replies라는 새로운 array를 만들어서 담도록 로직 구성

 </details>

<details>

<summary>
    
  ### 댓글 중복 출력 문제
  
</summary>

  #### 문제

  replies에 담긴 댓글들이 화면에 중복 출력되는 문제발생

  #### 해결

  게시글 상세 serializer에 get_comments 함수로 is_reply가 아닌 코멘트만 필터해서 불러오도록 로직 변경

</details>

<details>

<summary>
  
  ### 로그인 관련 트러블슈팅
  
</summary>

  #### 문제

  토큰 로그인 방식은 세션 로그인 방식에서 쓰던 request.user.is_authenticated 사용 불가능

  #### 해결

  직접적으로 html에 로그인을 했다는 사실을 전달해줘야함. 로그인 할 때 username도 같이 받아서 local storage에 저장 후 localstorage에 username이 존재여부에 따라 로그인 여부를 확인 함

</details>

<details>

<summary>
  
  ### 개발용 설정파일과 배포용 설정파일의 차이(settings.py)
  
</summary>

  #### 문제

설정 파일 중 settings.py에 들어가는 소스코드가 개발용과 실제 배포용에서는 차이가 발생함

#### 해결

- 개발용
    
    Debug = True
    
    Allowed_Hosts = [ ]
    
- 배포용
    
    Debug = False
    
    Allowed_Hosts = [ “x.x.x.x”, “127.0.0.1”, “localhost”, ]

</details>

<details>
  <summary>

  ### https 적용 관련 트러블 슈팅

  </summary>

  #### 문제

  기존의 http에서 보안상의 이슈로 https를 적용하려했으나 잘 적용되지않았음

  #### 해결

  AWS에서 Certificate Manager를 통해 SSL 인증서를 발급받고, 이를 적용한 로드밸런서를 생성하고 EC2 인스턴스에 연동함.
  위의 과정만 진행하면 되었지만 잘모르는 상태라 NGINX.conf 에서도 설정을 해서 이중으로 동작하여 504 bad gateway 에러가 발생하였기때문에, NGINX 설정은 기본값으로 원상복구함.

</details>

</details>



<br>

<br>

## 협업 방식
### 매일 아침 회의마다 daily task 공유(figma 활용)
![피그마_1](https://github.com/JWTONE/VITA-INFO/assets/159910835/f19a0f99-defe-457a-9601-c28d4ff6fdd5)
![피그마_2](https://github.com/JWTONE/VITA-INFO/assets/159910835/728e3e29-d78a-4960-81c2-d24a7d107556)
