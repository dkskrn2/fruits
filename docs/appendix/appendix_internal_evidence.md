# 내부 근거 정리

## 1. 목적
- 현재 폴더 내부 문서에서 인용 가능한 핵심 팩트를 추출해 외부 조사와 분리한다.
- 기존 전략 자산과 미검증 가정을 구분한다.

## 2. 기준선 문서
- 현재 전략 표현 기준선: `output/business_plan.html`
- 범용 사업기획 구조 참고: `business_proposal_plan.md`
- 전략 자산: `strategy/business_strategy.md`
- 연구 자산: `research/*.md`, `analysis/swot_pest_analysis.md`
- 사용자 탐색 메모: `input/0308/resorce.md`

## 3. 핵심 팩트

### 시장/수요
| ID | 팩트 | 근거 |
|----|------|------|
| IE-001 | 온라인 식료품 시장은 고성장 구간으로 해석되고 있다. | `research/ecommerce_trends.md` |
| IE-002 | 과일 소비 트렌드는 고당도, 신품종, 프리미엄, 건강 중심으로 이동 중이라는 내부 가설이 일관되게 반복된다. | `research/market_overview.md`, `analysis/swot_pest_analysis.md`, `output/business_plan.html` |
| IE-003 | 소비 양극화로 프리미엄과 가성비 상품이 동시에 성장한다는 관점이 문서 전반에서 반복된다. | `research/market_overview.md`, `research/ecommerce_trends.md` |
| IE-004 | 온라인 식료품 구매자의 정기 구매 비중 37%는 내부 전략의 핵심 숫자로 반복 인용된다. | `research/ecommerce_trends.md`, `research/b2c_consumer.md`, `analysis/swot_pest_analysis.md`, `output/business_plan.html` |
| IE-005 | 1인 가구와 맞벌이 가정은 소포장, 간편 과일, 정기배송 친화 세그먼트로 정의되어 있다. | `research/b2c_consumer.md` |

### 경쟁 구도
| ID | 팩트 | 근거 |
|----|------|------|
| IE-006 | 컬리는 프리미엄 큐레이션 강점, 오아시스는 가성비+건강, 쿠팡은 물류와 가격 경쟁력이 핵심 포지션으로 정리돼 있다. | `research/competitor_analysis.md` |
| IE-007 | 내부 문서는 “과일 전문 플랫폼”이 아직 충분히 선점되지 않았다고 본다. | `research/competitor_analysis.md`, `analysis/swot_pest_analysis.md` |
| IE-008 | 대형 플랫폼의 위협은 가격 횡포와 범용 플랫폼화로 정리된다. | `analysis/swot_pest_analysis.md`, `output/business_plan.html` |
| IE-009 | B2B 온라인도매 전환은 초기 시장으로 해석되어 선점 가능성이 있다고 본다. | `research/b2b_market.md`, `analysis/swot_pest_analysis.md` |

### 소비자 가치 제안
| ID | 팩트 | 근거 |
|----|------|------|
| IE-010 | 내부 전략 문서의 B2C 핵심 정의는 “과일은 정보재가 아닌 경험재”다. | `strategy/business_strategy.md` |
| IE-011 | 신뢰 장치는 당도 보증, 선별 데이터 공개, 농가 실명 공개로 구체화되어 있다. | `strategy/business_strategy.md`, `output/business_plan.html` |
| IE-012 | 첫 구매 경험, 배송 품질, 맛의 일관성, 빠른 CS가 재구매를 좌우한다. | `research/b2c_consumer.md` |
| IE-013 | 과일 취향 테스트, 품종 기반 큐레이션, 상황별 구매 비서는 차별 서비스 후보로 정리돼 있다. | `strategy/business_strategy.md`, `output/business_plan.html` |

### B2B 가치 제안
| ID | 팩트 | 근거 |
|----|------|------|
| IE-014 | B2B 고객의 상위 의사결정 요인은 가격, 품질 일관성, 공급 안정성, 결제 조건, 배송 신뢰성이다. | `research/b2b_market.md` |
| IE-015 | B2B 핵심 기능은 대량 주문, 견적, 계약 거래, 여신, 품질 인증, 산지 이력 추적이다. | `research/b2b_market.md`, `strategy/business_strategy.md` |
| IE-016 | 기존 전화/카톡 발주 습관이 디지털 전환 장벽으로 인식된다. | `analysis/swot_pest_analysis.md`, `output/business_plan.html` |
| IE-017 | 카카오톡 발주 봇과 POS 연동 자동발주가 장벽 완화용 솔루션으로 제시돼 있다. | `strategy/business_strategy.md` |

### 운영/물류
| ID | 팩트 | 근거 |
|----|------|------|
| IE-018 | 내부 전략의 진짜 핵심은 “수요 예측과 폐기율 최소화”다. | `strategy/business_strategy.md` |
| IE-019 | 구독과 B2B 계약 발주는 베이스 수요를 만드는 운영 장치로 정의된다. | `strategy/business_strategy.md` |
| IE-020 | A/B/C 등급 자동 라우팅으로 폐기를 줄이는 구조가 전략의 운영 핵심이다. | `strategy/business_strategy.md`, `output/business_plan.html` |
| IE-021 | Hub & Spoke 전환, 소포장 라인, 구독 박스 라인은 기존 오프라인 창고 활용 전략과 연결된다. | `strategy/business_strategy.md` |
| IE-022 | 품질 관리에서 당도, 외관, 포장, 온도 모니터링, 사진 기반 AI CS가 모두 중요한 축으로 정의된다. | `strategy/business_strategy.md` |

### 기술/데이터
| ID | 팩트 | 근거 |
|----|------|------|
| IE-023 | 과일 카테고리는 산지, 크기, 당도 등 정량 지표가 있어 데이터화에 유리하다는 내부 논리가 있다. | `strategy/business_strategy.md` |
| IE-024 | 초기 기술 전략은 전면 AI가 아니라 Rule-based와 데이터 수집부터 시작하는 단계적 도입이다. | `strategy/business_strategy.md`, `output/business_plan.html` |
| IE-025 | 당도 DB, 품종 데이터, 재구매율, 리뷰 감정 데이터는 장기적 해자 후보로 정의된다. | `strategy/business_strategy.md`, `output/business_plan.html` |

### 사용자 메모 기반 시사점
| ID | 팩트 | 근거 |
|----|------|------|
| IE-026 | 사용자 메모는 일반가/도매가 분리, 가격 변동 차트, 백오피스, SNS 활용, ERP 수요예측을 중요한 요구로 본다. | `input/0308/resorce.md` |
| IE-027 | “입문 세트”, “샘플링”, “구독”, “펫용 과일”, “기부 스토리”는 차별 상품 아이디어로 제시돼 있다. | `input/0308/resorce.md` |
| IE-028 | 소비자는 품종과 산지 차이를 잘 모른다는 점이 교육형 커머스 기회로 읽힌다. | `input/0308/resorce.md` |
| IE-029 | 딸기, 귤, 바나나, 고구마, 스테비아 토마토처럼 품종/당도/브랜드/산지 서사가 구매 동기가 될 수 있다는 관찰이 있다. | `input/0308/resorce.md` |

## 4. 내부 문서의 반복 논리
1. 과일은 반복 구매와 데이터 표준화가 가능한 카테고리다.
2. B2B와 B2C를 동시에 가져가야 운영 안정성과 수익성을 같이 잡을 수 있다.
3. 차별화의 핵심은 “당도/품종/큐레이션/선물 경험”과 “Zero-CAC B2B to B2C 전환”이다.
4. 기술의 핵심은 화려한 AI가 아니라 수요예측과 폐기 통제다.

## 5. 미검증 가정과 주의점
| ID | 항목 | 상태 | 비고 |
|----|------|------|------|
| IA-001 | 기존 거래처 수, 창고 평수, 연매출, 월 취급 물량 | 미검증 | `OOO`, `OO평`, `OO톤`, `OO억` placeholder 존재 |
| IA-002 | “8~10개월 BEP 가능” | 미검증 | 재무 근거 문서 없음 |
| IA-003 | “공헌이익률 27.5%” | 미검증 | 산출식 없음 |
| IA-004 | “매입원가 55% 방어 가능” | 미검증 | 경쟁사 비교 근거 미흡 |
| IA-005 | “B2B 거래처를 B2C로 Zero-CAC 전환” | 부분 검증 | 논리상 유효하지만 실증 데이터 필요 |

## 6. 내부 근거가 주는 현재 결론
- 현재 내부 자산만으로도 “프리미엄 과일 전문 + 데이터 큐레이션 + B2B/B2C 듀얼 모델”이라는 전략 방향은 충분히 선명하다.
- 다만 온브릭스를 실제로 넘어서는 제안서가 되려면, 외부 기준선에서 온브릭스의 강점과 약점을 정밀하게 분해해야 한다.
- 스마트스토어 실제 상품 패턴과 가격/리뷰 구조를 외부 데이터로 보완해야 전략의 현실성이 생긴다.
