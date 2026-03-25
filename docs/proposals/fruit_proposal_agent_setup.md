# 온라인 과일 커머스 제안 문서 에이전트 운영 설정

## 1. 목적
- 본 문서는 `online_fruit_commerce_proposal_execution_plan.md`를 실제로 실행하기 위한 에이전트 운영 체계를 정의한다.
- 목표는 넓게 훑는 조사보다, **온브릭스를 넘어서는 전략을 도출할 만큼 깊이 있는 조사와 판단**을 수행하는 것이다.

## 2. 운영 원칙
- 내부 문서 우선: 현재 폴더 내 문서를 먼저 근거화한다.
- 폭보다 깊이: 경쟁사는 10개를 깊게 본다.
- 탐색과 판단 분리: 자료 수집 단계와 전략 판단 단계를 섞지 않는다.
- 근거 없는 주장 금지: 전략 문장마다 근거 로그나 비교표를 연결한다.
- 중간 산출물도 모두 `md`로 남긴다.

## 3. 기준 문서
- 실행 기준 문서: `online_fruit_commerce_proposal_execution_plan.md`
- 현재 상황 기준선: `output/business_plan.html`
- 과거 범용 플랜 참고: `business_proposal_plan.md`
- 기존 전략 자산 참고: `strategy/business_strategy.md`
- 사용자 탐색 메모 참고: `input/0308/resorce.md`

## 4. 에이전트 구성

### Agent 0. Orchestrator
- 역할: 전체 우선순위 조정, 산출물 품질 관리, 단계 종료 승인
- 입력:
  - 전체 계획 문서
  - 각 에이전트 중간 산출물
- 출력:
  - 주차별 진행 상태
  - 누락 항목 리스트
  - 최종 통합 방향
- 핵심 책임:
  - 탐색 폭이 과도해지면 범위를 줄인다.
  - 에이전트 간 충돌하는 가설을 정리한다.
  - 최종 전략 3안을 비교 가능한 형식으로 정리한다.
- 종료 조건:
  - 본문/부록에 필요한 모든 원천 산출물이 준비됨

### Agent 1. Internal Evidence Agent
- 역할: 내부 문서와 PDF에서 인용 가능한 팩트를 체계적으로 추출
- 입력:
  - `research/`
  - `analysis/`
  - `strategy/`
  - `output/business_plan.html`
  - `input/*.pdf`
  - `input/0308/resorce.md`
- 출력:
  - `appendix_internal_evidence.md`
- 핵심 책임:
  - 기존 문서의 핵심 주장, 수치, 가정, 표현을 분리 추출
  - placeholder 수치(`OOO`, `OO평`)와 검증 필요 주장 표시
  - 현재 전략 자산과 공백 영역 구분
- 종료 조건:
  - 인용 가능한 팩트 100개 이상 정리
  - 내부 근거와 미검증 가정이 분리됨

### Agent 2. Keyword Discovery Agent
- 역할: Google/Naver 기반 키워드 탐색과 시장 신호 수집
- 입력:
  - Seed 키워드 세트
  - 내부 문서에서 나온 핵심 가설
- 출력:
  - `appendix_research_log.md`
- 핵심 책임:
  - 검색 로그를 관점별로 분류
  - 소비자 언어와 판매자 언어를 구분
  - 신규 인사이트가 줄어들면 포화 기준에 따라 종료
- 종료 조건:
  - 로그 120건 이상
  - 반복/광고성/저신뢰 자료 정리 완료

### Agent 3. Onbricks Benchmark Agent
- 역할: 온브릭스를 기준선으로 해부하고, 우리가 반드시 넘어야 하는 축을 정의
- 입력:
  - 온브릭스 공개 정보
  - 내부 문서의 온브릭스 관련 가설
- 출력:
  - `appendix_onbricks_benchmark.md`
- 핵심 책임:
  - 포지션, 핵심전략, 가격 구조, 상품 표현 방식, 브랜드 메시지, 차별점, 약점 정리
  - 온브릭스의 강한 축과 취약 축을 분리
  - “이기려면 어디에서 이겨야 하는가”를 명문화
- 종료 조건:
  - 온브릭스 기준선 표 완성
  - 정량/정성 비교 KPI 초안 완성

### Agent 4. Competitor Deep Dive Agent
- 역할: 핵심 경쟁사 10개를 심층 분석
- 입력:
  - 온브릭스 기준선
  - 경쟁사 후보 리스트
- 출력:
  - `appendix_competitor_benchmark.md`
- 핵심 책임:
  - 각 경쟁사별 아래 항목을 동일 포맷으로 기록
  - `포지션`, `핵심전략 3개`, `가격대 구간 3개`, `대표 SKU 3개`, `배송 정책`, `상세페이지 특징`, `리뷰 장치`, `구독/멤버십/CRM`, `강점 3개`, `약점 3개`, `온브릭스 대비`
- 종료 조건:
  - 핵심 경쟁사 10개 완성
  - 루브릭 평균 75점 이상

### Agent 5. Smartstore Merchandising Agent
- 역할: 네이버 스마트스토어 인기 카테고리와 대표 상품 패턴 분석
- 입력:
  - 카테고리 후보
  - 키워드 로그
- 출력:
  - `appendix_smartstore_catalog.md`
- 핵심 책임:
  - 카테고리별 가격대, 썸네일 문법, 제목 키워드, 후기 포인트, 배송 조건 추출
  - 어떤 상품이 많이 팔리는지보다 “왜 그 표현이 먹히는지”를 해석
  - 대표 카테고리 8~10개를 정밀 분석
- 종료 조건:
  - 상품 160개 이상 구조화
  - 카테고리별 반복 패턴 요약 완료

### Agent 6. Strategy Architect Agent
- 역할: 수집된 근거를 바탕으로 전략 3안을 설계
- 입력:
  - 내부 근거
  - 키워드 로그
  - 온브릭스 벤치마크
  - 경쟁사 심층 비교
  - 스마트스토어 패턴 분석
- 출력:
  - `final_online_fruit_commerce_proposal.md`
- 핵심 책임:
  - 전략 A/B/C를 구체 전략안으로 승격
  - 각 전략안의 타겟, 핵심 가치, 상품 구조, 가격 전략, 성장 채널, 운영 난이도, 리스크 정리
  - 추천 1안을 선정하고 90일 액션 플랜 제시
- 종료 조건:
  - 전략 3안 비교표 완성
  - 추천안 1개와 선택 이유 확정

### Agent 7. QA and Fact Check Agent
- 역할: 최종 문서 검증
- 입력:
  - 본문과 모든 부록
- 출력:
  - `appendix_validation_notes.md`
- 핵심 책임:
  - 주장-근거 연결 여부 확인
  - placeholder, 중복 주장, 모순, 과장 문구 제거
  - 온브릭스 초과 달성 논리의 빈 구멍 표시
- 종료 조건:
  - 검증 메모 반영 후 치명적 공백 0건

## 5. 실행 순서
1. `Agent 0`이 범위와 산출물 형식을 고정한다.
2. `Agent 1`이 내부 근거를 먼저 정리한다.
3. `Agent 2`가 외부 키워드 탐색 로그를 만든다.
4. `Agent 3`이 온브릭스 기준선을 만든다.
5. `Agent 4`가 경쟁사 10개를 같은 포맷으로 깊게 비교한다.
6. `Agent 5`가 스마트스토어 카테고리와 상품 표현 패턴을 정리한다.
7. `Agent 6`이 전략 3안과 추천안을 작성한다.
8. `Agent 7`이 검증 후 수정 사항을 반환한다.
9. `Agent 0`이 최종본을 승인한다.

## 6. 산출물 맵
- 본문:
  - `final_online_fruit_commerce_proposal.md`
- 부록:
  - `appendix_internal_evidence.md`
  - `appendix_research_log.md`
  - `appendix_onbricks_benchmark.md`
  - `appendix_competitor_benchmark.md`
  - `appendix_smartstore_catalog.md`
  - `appendix_validation_notes.md`

## 7. 검토 결과 반영 사항
- 현재 계획은 방향은 맞지만, 수행 책임이 분리되지 않아 실제 실행시 누락 위험이 있었다.
- `business_proposal_plan.md`는 범용 사업기획서용 구조라 현재의 딥 리서치형 커머스 제안 작업과는 다소 다르다.
- `strategy/business_strategy.md`는 유용한 전략 자산이지만 placeholder 수치와 오탈자가 남아 있어 그대로 기준선으로 쓰면 위험하다.
- 따라서 본 작업의 기준 체계는 `online_fruit_commerce_proposal_execution_plan.md + fruit_proposal_agent_setup.md` 조합으로 운영한다.

## 8. 운영 메모
- 경쟁사 수를 늘리는 대신, 반드시 10개를 동일 프레임으로 끝까지 채운다.
- 스마트스토어도 카테고리 수보다 패턴 해석을 우선한다.
- 전략 문서 작성 전에 반드시 온브릭스 기준선 표가 먼저 완성되어야 한다.
