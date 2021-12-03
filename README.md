# 📒 밀리의 서재 모티브의 전자책 구독 플랫폼 프로젝트 소개

### 독서와 무제한 친해지리, 전자책 구독서비스 밀리의 서재 어플리케이션을 모티브로 한 전자책 구독 플랫폼 구현

## 프로젝트 소개
'밀리의 서재' 어플리케이션을 벤치마킹하여 전자책 구독 플랫폼 서비스를 구축했습니다. <br>
애자일 방법론을 채택하여 연휴를 제외하고 총 2주 간 스프린트 방식으로 프로젝트를 진행했습니다.<br>
사용자에게 편리한 서비스를 제공할 수 있는 방법을 고민하고 실행에 옮기는 것을 기초 목적으로 삼았습니다.<br><br>
효율적인 아키텍처 구축, 사용자 중심의 다양한 서비스를 제공하기 위해 효율적인 데이터 모델링 방안을 고민했습니다.<br>
최적화된 데이터베이스 사용을 목적으로 장고 ORM을 사용하였고,<br>
AWS의 RDS, EC2, S3버킷 등을 사용하여 시스템 아키텍쳐를 설계했습니다.<br>
각 기능에 대해 유닛테스트를 진행하여 여러 환경 변수에 대한 안정성을 확보했습니다. <br><br>

## BACKEND 개발팀
|이름   |담당 기능|
|-----|------------------------------|
|박지원 |DB 모델링,나의 서재와 책장기능 로직 구현|
|신우주 |DB 모델링, 소셜로그인, 뷰어기능 로직 구현|
|이무현 |DB 모델링, 메인,상세페이지 로직 구현, AWS 배포|


## 개발기간
- 2021/09/13 ~ 2021/10/1 (연휴기간 제외)

## 시연 영상

<div id=header align="center">
  <a href="https://www.youtube.com/watch?v=WJS8kuzjzJU">👉🏻 시연 영상 보러가기</a>
</div>

## 사용 기술 및 tools
### Backend
- Python
- Django
- Mysql

### ETC
- Git
- Github
- POSTMAN

## 모델링
<p align="center"><img src="https://user-images.githubusercontent.com/80395324/144553831-a53341da-b82d-4c37-ad69-992427015db3.png" width="1000" height="700"/></p>


## 구현기능
### 회원별 서재 및 책장
- 회원이 최초 로그인을 하면, 유저 별 1개의 서재가 자동적으로 생성되도록 기능을 구현하였습니다. 
- 유저는 1개의 서재를 가지고 있고, 서재에는 여러 책장이 존재합니다.
- 해당 도서를 서재에 담고 있는 모든 유저의 닉네임과 프로필, 모든 유저의 수를 카운트하여 반환합니다.
- 책장에 도서를 담을 수 있습니다. 책장이나 도서의 입력값이 없을 경우, 이미 책장에 같은 도서가 담겨있는 경우는 에러를 반환합니다.
- 책장 추가와 삭제가 가능합니다. 책장의 입력값이 없을 경우, 추가하려는 책장의 이름이 이미 존재하는 경우는 에러를 반환합니다.
- 해당 유저가 가지고 있는 책장의 이름과 책장의 아이디를 반환합니다.
- 서재에 존재하는 모든 도서에 대하여 중복없이 도서 정보(아이디, 이름, 도서이미지, 저자, 페이지, 출판사, 출판일, 즐겨찾기)를 반환합니다.
- 책장 별 도서 상세 조회 기능을 구현하였습니다. 읽고 있는 책, 즐겨찾기의 책을 True or False 로 필터링하여 도서정보를 반환하며, 책장 별 도서 정보도 추가로 반환합니다.

## API
[POSTMAN API 문서 보러가기](https://documenter.getpostman.com/view/17234812/UVJfkbQ2)


## 폴더 구조
```bash
├── README.md
├── __pycache__
├── books
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_initial.py
│   │   ├── 0003_alter_bookinfo_contents.py
│   │   ├── 0004_alter_bookinfo_contents.py
│   │   ├── 0005_alter_book_description.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── core
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── libraries
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── my_settings.py
├── pull_request_template.md
├── requirements.txt
├── tnb
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── decorators.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## TIL정리 (Blog)
- 회고록 : 
- 리팩토링 : 
- 관련기술 : 

## ❗️ Reference
이 프로젝트는 밀리의 서재 어플리케이션을 참조하여 학습목적으로 만들었습니다.
실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
