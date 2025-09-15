# 🛒 온라인 쇼핑몰 프로젝트 (Django)

---

### 🌟 프로젝트 소개
이 프로젝트는 **Django와 Python**을 활용하여 사용자 친화적인 **온라인 쇼핑몰**을 구축한 예제입니다.  

기본적인 전자상거래 기능(회원가입, 로그인, 장바구니, 결제)을 직접 구현하여 **웹 개발 전반**을 경험하고,  
동시에 **Playwright 기반 웹 자동화 테스트**를 적용하기 위해 설계되었습니다.  

👉 기존의 공개된 웹사이트가 아닌, **제가 직접 제작한 서비스 환경에서 QA 자동화 테스트를 해보고 싶다는 탐구심으로 제작**했다는 점이 가장 큰 특징입니다.


*연계 프로젝트: [qa-automation-playwright](https://github.com/euuuuuuan/qa-automation-playwright)

---

### 🚀 주요 기능
- ✅ **사용자 인증**: Django 기본 인증 시스템 기반 회원가입 및 로그인  
- ✅ **상품 관리**: 상품 목록 조회, 상세 페이지 제공  
- ✅ **장바구니**: 상품 담기, 수량 변경, 삭제 기능  
- ✅ **주문/결제**: 장바구니 상품 주문 및 완료 처리  
- ✅ **관리자(Admin)**: 관리자 페이지에서 상품, 주문, 사용자 데이터를 관리  

---

### 🖼️ 구현된 웹 페이지 미리보기

아래는 Django 기반으로 구현한 온라인 쇼핑몰 웹사이트의 주요 화면입니다.  
각 화면은 실제 Playwright 자동화 테스트 대상(SUT)으로 사용되었습니다.

#### 🏠 메인 페이지
<img src="https://github.com/user-attachments/assets/2f5ec65a-5c50-420c-8451-461155384a85" alt="랜딩 페이지" width="300"/>

#### 👕 상품 상세 페이지
<img src="https://github.com/euuuuuuan/qa-e-commerce-site-django/blob/main/docs/screenshots/detail_page.png" alt="상세 페이지" width="300"/>

#### 🛒 장바구니 페이지
<img src="https://github.com/euuuuuuan/qa-e-commerce-site-django/blob/main/docs/screenshots/cart_page.png" alt="장바구니 페이지" width="300"/>

#### 💳 주문 완료 페이지
<img src="https://github.com/euuuuuuan/qa-e-commerce-site-django/blob/main/docs/screenshots/order_completed_page.png" alt="주문완료 페이지" width="300"/>

#### 📝 회원가입 페이지
<img src="https://github.com/euuuuuuan/qa-e-commerce-site-django/blob/main/docs/screenshots/register_page.png" alt="회원가입 페이지" width="300"/>

#### ⚙️ 관리자 페이지
<img src="https://github.com/euuuuuuan/qa-e-commerce-site-django/blob/main/docs/screenshots/admin_page.png" alt="관리자 페이지" width="300"/>

#### 📝 관리자 페이지 각종 정보확인
1) 계정 정보
<img src="https://github.com/euuuuuuan/qa-e-commerce-site-django/blob/main/docs/screenshots/account_info.png" alt="계정 정보" width="300"/>


2) 장바구니 정보
<img src="https://github.com/euuuuuuan/qa-e-commerce-site-django/blob/main/docs/screenshots/cart_info.png" alt="장바구니 정보" width="300"/>


3) 주문내역 정보
<img src="https://github.com/euuuuuuan/qa-e-commerce-site-django/blob/main/docs/screenshots/ordered_info.png" alt="주문내역 정보" width="300"/>


4) 상품 정보
<img src="https://github.com/euuuuuuan/qa-e-commerce-site-django/blob/main/docs/screenshots/prod_info.png" alt="상품 정보" width="300"/>






---

### 💡 기술적 성과 및 문제 해결
- ⚙️ **Django MTV 아키텍처 이해**: Model, Template, View를 활용한 웹 서비스 구조 설계  
- 🛠️ **문제 해결 경험**  
  - `405 오류`: HTML `form`의 `method`와 Django 뷰의 `@require_POST` 불일치 문제 해결  
  - 정적 파일(css, 이미지) 미적용 문제: `STATIC_URL`, `STATICFILES_DIRS` 최적화  
  - Pillow 모듈 미설치 → 이미지 처리 기능 오류 → 의존성 추가로 해결  
- 🗃️ **데이터베이스 연동**: SQLite 기반 상품, 주문, 장바구니 관리  
- 🖼️ **UI/UX 개선**: `landing.html`, `style.css` 수정으로 쇼핑몰 레이아웃 개선  

---

### 🤖 AI 도구 활용
본 프로젝트는 개발과 QA 과정에서 **AI 도구**를 적극 활용했습니다.  

- 📚 **학습 보조**: Django 핵심 개념 및 템플릿 문법 학습 시간 단축  
- ✨ **코드 품질 개선**: 뷰 함수 최적화, 템플릿 구조 개선  
- 🧩 **문제 해결**: 반복되는 오류(`405 Error`, `NameError`)를 AI와 함께 분석 및 해결  
- 📝 **문서화**: README와 실행 가이드 정리 자동화  

👉 사용한 도구: **ChatGPT, Claude, Google Gemini**  

---

### ⚙️ 개발 환경 및 기술 스택
- ![Python](https://img.shields.io/badge/Python-3.13.2-3776AB?style=flat-square&logo=python&logoColor=white)  
- ![Django](https://img.shields.io/badge/Django-5.2.6-092E20?style=flat-square&logo=django&logoColor=white)  
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)  
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)  
- ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)  
- ![Pillow](https://img.shields.io/badge/Pillow-Image%20Library-yellow?style=flat-square)  

---

### ▶ 실행 방법

1️⃣ 프로젝트 클론  

[git clone](https://github.com/euuuuuuan/qa-e-commerce-site-django.git)


2️⃣ 가상환경 생성 및 활성화

```
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
3️⃣ 의존성 설치

```
pip install -r requirements.txt
# 또는
pip install Django Pillow
```
4️⃣ 데이터베이스 마이그레이션

```
python manage.py makemigrations
python manage.py migrate
```
5️⃣ 슈퍼유저 생성 (관리자 계정)

```
python manage.py createsuperuser
```
6️⃣ 서버 실행

```
python manage.py runserver
```
7️⃣ 접속

```
http://127.0.0.1:8000/
```

📂 프로젝트 구조
```
clothing-mall-project/
 ┣ 📂 myshop/                  # 프로젝트 설정
 ┣ 📂 shop/                    # 쇼핑몰 앱
 ┃ ┣ 📂 migrations/
 ┃ ┣ 📂 static/shop/
 ┃ ┃ ┣ 📂 images/
 ┃ ┃ ┗ style.css
 ┃ ┣ 📂 templates/shop/
 ┃ ┣ admin.py
 ┃ ┣ models.py
 ┃ ┣ urls.py
 ┃ ┗ views.py
 ┣ 📂 venv/                    # 가상 환경
 ┣ 📂 docs/screenshots/
 ┣ db.sqlite3
 ┗ manage.py
```
---

### 🧑‍💻 개발자 정보

| 이름   | 역할               | 연락처                                                                 |
| :----- | :----------------- | :--------------------------------------------------------------------- |
| 전유안 | QA 자동화 엔지니어 | GitHub: [euuuuuuan](https://github.com/euuuuuuan)
