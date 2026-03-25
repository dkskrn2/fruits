# 과일다리 페이지 생성 실행 계획
## Fruitbridge Page Generation Implementation Plan

---

## 📋 프로젝트 개요
- **목표**: 60개 페이지 HTML 파일 생성 (UI만 구현, 기능 제외)
- **범위**: 사이트맵 기준 전체 페이지
- **접근방법**: 템플릿 기반 자동화 생성 + 수동 커스터마이징

---

## 🎯 실행 전략

### 1. 페이지 카테고리별 분류
- **완료된 페이지** (3개): 재사용 가능한 템플릿 추출
  - `/` - fruit_commerce_fruitbridge.html
  - `/impact` - fruit_commerce_impact.html
  - `/sitemap` - sitemap.html

- **생성 필요 페이지** (57개): 카테고리별 템플릿 적용
  - 상품 관련: 12개
  - 마이페이지: 15개
  - 구매 프로세스: 5개
  - 고객지원: 11개
  - 인증: 5개
  - 이벤트: 5개
  - 기타: 2개

### 2. 템플릿 패턴 정의

#### A. 기본 템플릿 구조
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{페이지명} - 과일다리</title>
    <style>
        /* 공통 CSS */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Pretendard', sans-serif; background: #f5f5f5; }
        .mobile-container {
            width: 430px;
            margin: 0 auto;
            background: white;
            min-height: 100vh;
        }
        /* 페이지별 CSS */
    </style>
</head>
<body>
    <div class="mobile-container">
        <!-- Header -->
        <!-- Content -->
        <!-- Bottom Navigation -->
    </div>
</body>
</html>
```

#### B. 페이지 타입별 템플릿

**1. 리스트형 페이지** (상품목록, 주문내역, 이벤트 등)
- 그리드/리스트 레이아웃
- 필터/정렬 UI
- 페이지네이션
- 카드형 아이템

**2. 폼 페이지** (회원가입, 주문서, 문의 등)
- 입력 필드
- 유효성 표시
- 단계 표시기
- 제출 버튼

**3. 상세 페이지** (상품상세, 이벤트상세 등)
- 이미지 갤러리
- 정보 섹션
- 액션 버튼
- 탭/아코디언

**4. 대시보드 페이지** (마이페이지, 메인 등)
- 요약 카드
- 빠른 메뉴
- 최근 활동
- 통계 위젯

**5. 정보형 페이지** (약관, 가이드 등)
- 텍스트 콘텐츠
- 목차
- 아코디언 FAQ
- 다운로드 링크

---

## 🤖 에이전트 및 도구 활용 전략

### Phase 1: 템플릿 준비 (수동)
**도구**: Read, Write, Edit
1. 기존 3개 HTML 파일에서 공통 컴포넌트 추출
2. 베이스 템플릿 파일 생성 (base_template.html)
3. 페이지 타입별 템플릿 5개 생성

### Phase 2: 자동 생성 (Agent 활용)
**에이전트**: general-purpose agent
**역할**: 템플릿 기반으로 페이지 대량 생성

```python
# 페이지 생성 스크립트 (create_pages.py)
import pandas as pd
import os

# CSV 읽기
df = pd.read_csv('ia_structure_enhanced.csv')

# 템플릿 매핑
template_map = {
    '리스트': ['상품메인', '전체상품', '베스트', '주문내역', '이벤트메인'],
    '폼': ['회원가입', '로그인', '주문서작성', '1:1문의'],
    '상세': ['상품상세', '이벤트상세'],
    '대시보드': ['메인페이지', '마이페이지메인'],
    '정보': ['이용약관', '개인정보처리방침', 'FAQ']
}

# 페이지별 HTML 생성
for index, row in df.iterrows():
    if row['상태'] != '완료':
        generate_page(row)
```

### Phase 3: 페이지별 커스터마이징
**도구**: Edit, Write
1. 생성된 각 페이지 검토
2. 페이지별 고유 콘텐츠 추가
3. 스타일 조정

---

## 📁 폴더 구조

```
C:/Users/dkskr/OneDrive/111/fruits/
├── output/
│   ├── pages/                    # 생성될 모든 페이지
│   │   ├── home/
│   │   │   ├── index.html       # 메인페이지
│   │   │   └── impact.html      # 소셜임팩트
│   │   ├── products/
│   │   │   ├── index.html       # 상품메인
│   │   │   ├── all.html         # 전체상품
│   │   │   ├── family.html      # 가족루틴
│   │   │   ├── kids.html        # 아이간식
│   │   │   ├── greeting.html    # 안부전하기
│   │   │   ├── donation.html    # 나눔과일
│   │   │   ├── seasonal.html    # 제철과일
│   │   │   ├── best.html        # 베스트
│   │   │   ├── new.html         # 신상품
│   │   │   ├── detail.html      # 상품상세 (템플릿)
│   │   │   └── search.html      # 상품검색
│   │   ├── order/
│   │   │   ├── cart.html        # 장바구니
│   │   │   ├── checkout.html    # 주문서작성
│   │   │   ├── payment.html     # 결제
│   │   │   └── complete.html    # 주문완료
│   │   ├── mypage/
│   │   │   ├── index.html       # 마이페이지메인
│   │   │   ├── orders.html      # 주문내역
│   │   │   ├── delivery.html    # 배송조회
│   │   │   ├── wishlist.html    # 찜목록
│   │   │   ├── reviews.html     # 리뷰관리
│   │   │   ├── coupons.html     # 쿠폰함
│   │   │   ├── points.html      # 포인트
│   │   │   ├── profile.html     # 회원정보
│   │   │   ├── address.html     # 배송지관리
│   │   │   ├── subscription.html # 정기배송
│   │   │   └── donation-history.html # 나눔내역
│   │   ├── event/
│   │   │   ├── index.html       # 이벤트메인
│   │   │   ├── ongoing.html     # 진행중이벤트
│   │   │   ├── ended.html       # 종료된이벤트
│   │   │   ├── winners.html     # 당첨자발표
│   │   │   └── detail.html      # 이벤트상세
│   │   ├── support/
│   │   │   ├── index.html       # 고객지원메인
│   │   │   ├── faq.html         # FAQ
│   │   │   ├── inquiry.html     # 1:1문의
│   │   │   ├── notice.html      # 공지사항
│   │   │   ├── guide.html       # 이용가이드
│   │   │   ├── terms.html       # 이용약관
│   │   │   ├── privacy.html     # 개인정보처리방침
│   │   │   ├── delivery-policy.html # 배송정책
│   │   │   ├── return-policy.html   # 교환/반품정책
│   │   │   ├── storage-guide.html   # 보관가이드
│   │   │   └── brix-guide.html      # 당도가이드
│   │   ├── auth/
│   │   │   ├── login.html       # 로그인
│   │   │   ├── signup.html      # 회원가입
│   │   │   ├── find-id.html     # 아이디찾기
│   │   │   ├── find-password.html # 비밀번호찾기
│   │   │   └── social-login.html  # 소셜로그인
│   │   └── etc/
│   │       ├── sitemap.html     # 사이트맵
│   │       └── search.html      # 통합검색
│   └── templates/                # 템플릿 파일
│       ├── base_template.html
│       ├── list_template.html
│       ├── form_template.html
│       ├── detail_template.html
│       ├── dashboard_template.html
│       └── info_template.html
└── scripts/
    └── generate_pages.py         # 페이지 생성 스크립트
```

---

## 🚀 실행 단계

### Step 1: 템플릿 생성 (30분)
1. 기존 HTML 분석 및 공통 요소 추출
2. 5개 템플릿 파일 생성
3. CSS/JS 라이브러리 정리

### Step 2: 폴더 구조 생성 (10분)
1. pages 폴더 및 하위 폴더 생성
2. templates 폴더 생성

### Step 3: Python 스크립트 작성 (20분)
1. CSV 데이터 읽기
2. 템플릿 매핑 로직
3. HTML 생성 함수

### Step 4: 자동 생성 실행 (Agent 사용, 1시간)
1. Agent에게 스크립트 실행 지시
2. 57개 페이지 자동 생성
3. 생성 결과 검증

### Step 5: 페이지별 커스터마이징 (2-3시간)
1. 카테고리별 페이지 검토
2. 더미 콘텐츠 추가
3. 페이지별 고유 스타일 적용

### Step 6: 네비게이션 연결 (30분)
1. 메뉴 링크 연결
2. 페이지간 이동 경로 설정
3. 뒤로가기 버튼 추가

---

## ⚡ 최적화 전략

### 1. 컴포넌트 재사용
- Header 컴포넌트
- Bottom Navigation
- 상품 카드
- 리스트 아이템
- 폼 필드

### 2. CSS 모듈화
- common.css: 공통 스타일
- layout.css: 레이아웃
- components.css: 컴포넌트
- page-specific.css: 페이지별

### 3. 더미 데이터 활용
```javascript
const products = [
  { id: 1, name: '제주 한라봉', price: 25000, brix: 13.5 },
  { id: 2, name: '나주 배', price: 18000, brix: 12.0 },
  // ...
];
```

---

## 📊 예상 결과물

### 생성될 파일
- HTML 파일: 60개
- 템플릿 파일: 6개
- CSS 파일: 4개
- 스크립트 파일: 1개

### 페이지 상태
- 완료: 60개 (UI만)
- 기능 구현: 0개 (향후 과제)

### 품질 기준
- ✅ 모바일 최적화 (430px)
- ✅ 일관된 디자인 시스템
- ✅ 페이지간 네비게이션
- ✅ 더미 콘텐츠 포함
- ❌ 실제 기능 (제외)
- ❌ 백엔드 연동 (제외)

---

## 🔧 도구 사용 계획

| 단계 | 주요 도구 | 에이전트 | 용도 |
|------|----------|---------|------|
| 1. 템플릿 준비 | Read, Write | - | 수동 작업 |
| 2. 스크립트 작성 | Write | - | Python 코드 작성 |
| 3. 대량 생성 | Task | general-purpose | 자동화 실행 |
| 4. 커스터마이징 | Edit, Write | - | 페이지 수정 |
| 5. 검증 | Read, Glob | - | 결과 확인 |

---

## 📝 추가 고려사항

1. **반응형 대응**: 현재 430px 고정, 향후 반응형 추가 가능
2. **다국어 지원**: 한국어 기본, 영어 버전 준비
3. **접근성**: ARIA 레이블, 시맨틱 HTML
4. **SEO**: meta 태그, 구조화된 데이터
5. **성능**: 이미지 최적화, lazy loading

---

## ⏰ 예상 소요시간
- 전체: 약 4-5시간
- 템플릿 준비: 30분
- 자동 생성: 1시간
- 커스터마이징: 2-3시간
- 검증 및 수정: 30분

---

이 계획에 따라 진행하면 효율적으로 60개 페이지를 생성할 수 있습니다.