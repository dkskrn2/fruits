# 🗺️ 과일다리 커머스 IA(Information Architecture) 구축 계획서

## 📋 프로젝트 개요
- **목적**: 과일다리 이커머스 사이트의 체계적인 사이트맵 및 IA 구조 정립
- **작성일**: 2024.12
- **범위**: 전체 사이트 구조 설계 및 URL 체계 수립

---

## 🎯 목표
1. **체계적인 사이트 구조 설계**
   - URL 단위의 명확한 페이지 구조
   - 일반 이커머스 표준 구조 적용
   - 과일다리 특화 기능 반영

2. **산출물 생성**
   - Excel 형식의 IA 문서
   - HTML 사이트맵 페이지
   - 페이지별 상세 스펙

---

## 🛠️ 활용 도구 및 에이전트

### 1. **파일 작업 도구**
- **Write Tool**: Excel 파일 생성 (CSV 형식)
- **Write Tool**: HTML 사이트맵 페이지 생성
- **Read Tool**: 기존 파일 분석

### 2. **분석 도구**
- **Grep Tool**: 기존 HTML 파일에서 링크 구조 파악
- **Glob Tool**: output 폴더 내 모든 HTML 파일 목록 확인

### 3. **에이전트 활용 계획**
- **general-purpose agent**:
  - 일반 이커머스 사이트 IA 베스트 프랙티스 조사
  - URL 네이밍 컨벤션 제안
  - SEO 최적화 구조 제안

---

## 📊 IA 구조 설계

### 1차 카테고리 (Main Categories)
```
1. 홈 (Home)
2. 상품 (Products)
3. 장바구니/주문 (Cart/Order)
4. 마이페이지 (My Page)
5. 이벤트/프로모션 (Events)
6. 고객지원 (Support)
7. 소셜임팩트 (Social Impact)
```

### URL 구조 체계
```
도메인: fruitbridge.com (가정)

/                           # 메인 홈
/products/                  # 상품 메인
/products/category/{name}   # 카테고리별 상품
/products/detail/{id}       # 상품 상세
/cart/                      # 장바구니
/order/                     # 주문
/mypage/                    # 마이페이지
/event/                     # 이벤트
/support/                   # 고객지원
/impact/                    # 소셜 임팩트
```

---

## 📝 작업 단계

### Phase 1: 분석 및 설계
1. **현재 상태 분석**
   - 기존 HTML 파일 구조 파악
   - 링크 관계 매핑
   - 누락된 페이지 식별

2. **IA 구조 설계**
   - 1차, 2차, 3차 depth 정의
   - URL 체계 수립
   - 페이지별 기능 정의

### Phase 2: 문서화
1. **Excel IA 문서 생성**
   - CSV 형식으로 생성 (Excel에서 열기 가능)
   - 컬럼: Depth1 | Depth2 | Depth3 | URL | 페이지명 | 설명 | 상태 | 비고

2. **HTML 사이트맵 페이지 생성**
   - 시각적 트리 구조
   - 클릭 가능한 링크
   - 개발 상태 표시

### Phase 3: 구현 가이드
1. **우선순위 정의**
   - P0: 필수 (메인, 상품, 장바구니)
   - P1: 중요 (마이페이지, 주문)
   - P2: 추가 (이벤트, 고객지원)

---

## 📊 예상 IA 구조

### Level 1 (최상위)
```
1. 홈 [/]
2. 상품 [/products]
3. 장바구니 [/cart]
4. 마이페이지 [/mypage]
5. 이벤트 [/event]
6. 고객지원 [/support]
7. 소셜임팩트 [/impact]
```

### Level 2 (상품 카테고리)
```
2.1 전체보기 [/products/all]
2.2 가족루틴 [/products/family]
2.3 아이간식 [/products/kids]
2.4 안부전하기 [/products/greeting]
2.5 나눔과일 [/products/donation]
2.6 제철과일 [/products/seasonal]
2.7 베스트 [/products/best]
2.8 신상품 [/products/new]
```

### Level 2 (마이페이지)
```
4.1 주문내역 [/mypage/orders]
4.2 배송조회 [/mypage/delivery]
4.3 찜목록 [/mypage/wishlist]
4.4 쿠폰/포인트 [/mypage/benefits]
4.5 리뷰관리 [/mypage/reviews]
4.6 회원정보 [/mypage/profile]
4.7 배송지관리 [/mypage/address]
```

### Level 2 (고객지원)
```
6.1 자주묻는질문 [/support/faq]
6.2 1:1문의 [/support/inquiry]
6.3 공지사항 [/support/notice]
6.4 이용가이드 [/support/guide]
6.5 배송안내 [/support/delivery-info]
6.6 교환/반품 [/support/return]
```

---

## 🎨 과일다리 특화 기능

### 특별 카테고리
- **나눔과일**: 구매 시 기부 연동
- **가족루틴**: 정기배송 특화
- **소비단위**: "4인 가족 7일분" 표시
- **당도보장**: Brix 기준 필터링

### 특별 페이지
- **소셜임팩트**: 기부 현황 및 스토리
- **보관가이드**: 과일별 보관법
- **엄마추천**: 타겟 특화 큐레이션

---

## 🚀 실행 계획

### Step 1: CSV 파일 생성
```python
# ia_structure.csv 생성
- 전체 사이트맵 데이터
- 페이지별 상세 정보
- 개발 상태 트래킹
```

### Step 2: HTML 사이트맵 생성
```html
# sitemap.html 생성
- 인터랙티브 트리 구조
- 개발 상태 시각화
- 링크 네비게이션
```

### Step 3: 검증 및 개선
- 사용자 플로우 검증
- SEO 최적화 확인
- 모바일 경험 최적화

---

## 📈 성공 지표
- [ ] 모든 주요 기능이 URL로 매핑됨
- [ ] 3-depth 이내의 간단한 구조
- [ ] 직관적인 URL 네이밍
- [ ] 확장 가능한 구조
- [ ] SEO 친화적 URL

---

## 🔄 다음 단계
1. CSV 형식의 IA 문서 생성
2. HTML 사이트맵 페이지 구현
3. 각 페이지 템플릿 생성 우선순위 결정
4. 개발 로드맵 수립

---

## 📌 참고사항
- 모바일 우선 설계 (430px 고정폭)
- 과일다리 브랜드 아이덴티티 유지
- 사회적 가치와 상업적 목표 균형
- 확장성 고려한 구조 설계