# 📒 밀리의 서재 모티브의 전자책 구독 플랫폼 프로젝트 소개

### 📍 프로젝트 개요
독서와 무제한 친해지리, 전자책 구독서비스 밀리의 서재 어플리케이션을 모티브로 한 전자책 구독 플랫폼 구현

### 📍 개발 인원과 기간

#### ✅ 개발팀
|이름   |담당 기능|
|-------|--------------------|
|박지원 |  |
|이무현 |   |
|신우주 |   |

##### ✅  개발기간
- 2021/09/13 ~ 2021/10/1 (연휴기간 제외)

##### ❗️ Reference
이 프로젝트는 밀리의 서재 어플리케이션을 참조하여 학습목적으로 만들었습니다.
실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.


<div id=header align="center">
  <a href="https://www.youtube.com/watch?v=WJS8kuzjzJU">👉🏻 시연 영상 보러가기</a>
</div>

<br>
<br>

### 📍 프로젝트 소개
'밀리의 서재' 어플리케이션을 벤치마킹하여 전자책 구독 플랫폼 서비스를 구축했습니다. <br>
애자일 방법론을 채택하여 연휴를 제외하고 총 2주 간 스프린트 방식으로 프로젝트를 진행했습니다. 사용자에게 편리하고 유용한 서비스를 제공할 수 있는 방법을 고민하고 실행에 옮기는 것을 기초 목적으로 삼았으며, 효율적인 아키텍처 구축을 위해 노력했습니다. <br><br>
백엔드팀에서는 사용자 중심의 다양한 서비스를 제공하기 위해 효율적인 데이터 모델링 방안을 고민했습니다. 최적화된 데이터베이스 사용을 목적으로 장고 ORM을 사용하였고, AWS의 RDS, EC2, S3버킷 등을 사용하여 시스템 아키텍쳐를 설계했습니다. 각 기능에 대해 유닛테스트를 진행하여 여러 환경 변수에 대한 안정성을 확보했습니다. <br><br>
프론트엔드팀에서는 React Hooks와 Styled-Component, 라이브러리 등을 이용하여 사용자의 흥미를 이끌어낼 수 있는 UI/UX를 구현했습니다. 직관적인 구조 파악과 재사용성을 염두에 두고 컴포넌트를 분리시켰으며, 동시에 API 통신으로 받은 데이터의 효율적 전달성을 확보했습니다.<br><br>



## 📅 Plan
✅ 프로젝트 수행 기간<br>
  2021.09.13 ~ 2021.10.1 (연휴기간 제외)

✅ 프로젝트 수행 방법
  애자일 방법론을 활용한 스크럼 방식 

<table style="text-align:center; margin:auto;">
  <tr>
    <th colspan="4" style="font-size:20px">1주차</th>
  </tr>
  <tr>
    <td colspan="4">
      <ul style="text-align:left">
        <li> FE - 소셜로그인, 메인페이지, 검색창 페이지 구현</li>
        <li> BE - 소셜로그인 통신확인, 데이터 모델링, 각 페이지 로직 구현</li>
      </ul>
    </td>
  </tr>
  <tr>
    <th colspan="4" style="font-size:20px">2주차</th>
  </tr>
  <tr>
    <td colspan="4">
      <ul style="text-align:left">
        <li> FE - 상세페이지, Nav & Footer, 뷰어 기능 등 구현, 동적 라우팅 구성 및 구동 확인</li>
        <li> BE - 배포 및 유닛테스트 </li>
      </ul>
    </td>
  </tr>
  </table>

<br>

## 📕 Teammate

<div id=teammate>
  <h4> 🎨 Front-End </h4>
  <table style="text-align:center;">
    <tr>
      <th><a href="https://github.com/janine-kang">강연옥</a></th>
      <th><a href="https://github.com/choseonghwan91">조성환</a></th>
      <th><a href="https://github.com/JUCHEOLJIN">주철진</a></th>
    </tr>
    <tr>
      <td>
       * 검색창 구현<br>
         - 카테고리별 검색<br>
         - 필터링 기능<br>
         - 검색결과 페이지<br>
       * 뷰어 기능 구현<br>
         - 한 쪽 보기/두 쪽 보기<br>
         - 목차기능<br>
         - 페이지 이동 기능<br>
      </td>
      <td>
       * Nav바 구현<br>
       * 소셜로그인 페이지 구현(Kakao)<br>
       * 나의 서재 페이지 구현<br>
         - 전체도서보기<br>
         - 나의 책장 보기<br>
      </td>
      <td>
       * 메인페이지 구현<br>
         - Carousel<br>
         - 도서 추천서비스<br>
         - 오늘의 도서 보기<br>
       * 상세페이지 구현<br>
         - 책 정보 보기<br>
         - 바로 읽기 기능<br>
         - 댓글 및 좋아요 기능<br>
         - 내 서재에 책 담기 기능<br>
         - 책장 추가 기능<br>
       * Footer 구현<br>
      </td>
    </tr>
  </table>
  <br>
  <h4> 🛢 Back-End </h4>
  <table style="text-align:center;">
    <tr>
      <th><a href="https://github.com/jiwon5304">박지원</a></th>
      <th><a href="https://github.com/shinwooju">신우주</a></th>
      <th><a href="https://github.com/PeterLEEEEEE">이무현</a></th>
    </tr>
    <tr>
      <td>
       * DB 모델링<br>
       * 나의 서재와 책장기능 로직 구현<br>
       * HTTP Methods 이용한 엔드포인트 구현 <br>
      </td>
      <td>
       * DB 모델링<br>
       * 소셜로그인(kakao)<br>
       * 데코레이터<br>
       * 뷰어기능 로직 구현, HTTP Methods 이용한 엔드포인트 구현 
      </td>
      <td>
       * DB 모델링<br>
       * 메인페이지와 상세페이지 로직 구현<br>
       * AWS 배포: RDS,S3 업로드, EC2 배포
      </td>
    </tr>       
  </table>
  <br>
  
</div>




## 과제 내용
> 아래 요구사항에 맞춰 게시판 Restfull API를 개발합니다.
- 에이모 선호 기술스택: python flask, mashmallow, mongoengine
- 필수 사용 데이터베이스: mongodb

### [필수 포함 사항]
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅

### [개발 요구사항]
- 원티드 지원 과제 내용 포함 (기본적인 게시판 글쓰기)
- 게시글 카테고리
- 게시글 검색
- 대댓글(1 depth)
    - 댓글 및 대댓글 pagination
- 게시글 읽힘 수
    - 같은 User가 게시글을 읽는 경우 count 수 증가하면 안 됨
- Rest API 설계
- Unit Test
- 1000만건 이상의 데이터를 넣고 성능테스트 진행 결과 필요


## 사용 기술 및 tools
> - Back-End :  <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/mongodb 5.0-1b9e41?style=for-the-badge&logo=Mongodb&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC :  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

## 모델링
![5 drawio](https://user-images.githubusercontent.com/8315252/139969615-38f01f08-cc1c-427e-87a6-09671525525b.png)

## API
[링크-postman document](https://documenter.getpostman.com/view/16042359/UVBzmpLX)

## 구현 기능
### 회원가입, 로그인
-
-

### 게시글 CRUD
-
-

### 댓글 대댓글 CRUD
-
-



## API TEST 방법
1. 우측 링크를 클릭해서 postman으로 들어갑니다. [링크](https://www.postman.com/wecode-21-1st-kaka0/workspace/assignment1-tw-jw-yy/overview)
2. 정의된 SERVER_URL이 올바른지 확인 합니다. (18.188.189.173:8000)
<img width="743" alt="스크린샷 2021-11-03 오전 12 23 05" src="https://user-images.githubusercontent.com/8219812/139912122-87d71d1d-d318-4057-8d76-f7311952ea75.png">

3. 정의된 회원가입, 로그인 요청을 이용해서 access_token을 획득합니다.

4. 각 요청에 header 부분에 Authorization 항목에 획득한 access_token을 입력하여 요청을 진행합니다. 회원가입, 로그인을 제외한 요청에는 access_token이 필요합니다.
<img width="1255" alt="스크린샷 2021-11-03 오전 1 58 17" src="https://user-images.githubusercontent.com/8219812/139912164-a5f49a32-5128-4902-a9d9-03dfa6a94672.png">

5. 만약 Send버튼이 비활성화가 될 시 fork를 이용해서 해당 postman project를 복사해서 시도하길 바랍니다.
![image](https://user-images.githubusercontent.com/8219812/139912241-d6cb5831-23e8-4cbb-a747-f52c42601098.png)


## 폴더 구조
```bash

```

## TIL정리 (Blog)
- 박지원 : https://yesjiwon5304.tistory.com/33

