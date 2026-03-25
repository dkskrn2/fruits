#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
프리미엄 과일 커머스 전략 제안서 - 전면 수정 버전
Opus 분석 결과를 완전히 반영한 현실적 버전
"""

import re

def create_revised_presentation():
    """전면 수정된 프레젠테이션 생성"""

    html_content = '''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>프리미엄 과일 커머스 - 현실적 전략 제안서 v3.0</title>
  <style>
    :root {
      --bg: #f5efe5;
      --paper: #fffaf3;
      --ink: #1f1a16;
      --muted: #675f56;
      --line: rgba(31, 26, 22, .10);
      --accent: #cb5b2c;
      --olive: #556548;
      --berry: #a14253;
      --gold: #a97828;
      --danger: #dc2626;
      --warning: #f59e0b;
      --success: #10b981;
      --shadow: 0 24px 60px rgba(43, 31, 18, .10);
      --display: "Iowan Old Style", "Palatino Linotype", "Apple SD Gothic Neo", "Malgun Gothic", serif;
      --body: "Noto Sans KR", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
    }

    * { box-sizing: border-box; }

    html { scroll-behavior: smooth; }

    body {
      margin: 0;
      font-family: var(--body);
      color: var(--ink);
      background: linear-gradient(135deg, #f7f1e7 0%, #f2ebdf 100%);
      overflow-x: hidden;
    }

    .presentation-container {
      width: 100vw;
      height: 100vh;
      position: relative;
      overflow: hidden;
    }

    .slide {
      position: absolute;
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transform: translateX(100%);
      transition: all 0.6s ease-in-out;
      padding: 40px;
    }

    .slide.active {
      opacity: 1;
      transform: translateX(0);
    }

    .slide.prev {
      transform: translateX(-100%);
    }

    .slide-content {
      max-width: 1200px;
      width: 100%;
      padding: 60px;
      background: var(--paper);
      border-radius: 20px;
      box-shadow: var(--shadow);
    }

    h1 {
      font-family: var(--display);
      font-size: 3em;
      margin: 0 0 20px 0;
      color: var(--ink);
      line-height: 1.2;
    }

    h2 {
      font-family: var(--display);
      font-size: 2.2em;
      margin: 0 0 30px 0;
      color: var(--ink);
    }

    h3 {
      font-size: 1.5em;
      margin: 20px 0;
      color: var(--accent);
    }

    .subtitle {
      font-size: 1.3em;
      color: var(--muted);
      margin-bottom: 40px;
    }

    .highlight {
      padding: 30px;
      background: linear-gradient(135deg, rgba(203, 91, 44, 0.1), rgba(203, 91, 44, 0.05));
      border-left: 4px solid var(--accent);
      border-radius: 10px;
      margin: 20px 0;
    }

    .warning-box {
      padding: 30px;
      background: linear-gradient(135deg, rgba(220, 38, 38, 0.1), rgba(220, 38, 38, 0.05));
      border-left: 4px solid var(--danger);
      border-radius: 10px;
      margin: 20px 0;
    }

    .success-box {
      padding: 30px;
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(16, 185, 129, 0.05));
      border-left: 4px solid var(--success);
      border-radius: 10px;
      margin: 20px 0;
    }

    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      margin: 30px 0;
    }

    .metric-card {
      padding: 25px;
      background: white;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }

    .metric-label {
      font-size: 0.9em;
      color: var(--muted);
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .metric-value {
      font-size: 2em;
      font-weight: bold;
      margin-bottom: 5px;
    }

    .metric-change {
      font-size: 0.9em;
      color: var(--success);
    }

    .metric-change.negative {
      color: var(--danger);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
    }

    th, td {
      padding: 15px;
      text-align: left;
      border-bottom: 1px solid var(--line);
    }

    th {
      background: rgba(203, 91, 44, 0.05);
      font-weight: 600;
    }

    .navigation {
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      gap: 15px;
      align-items: center;
      padding: 15px 25px;
      background: rgba(255, 255, 255, 0.95);
      border-radius: 50px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.1);
      z-index: 1000;
    }

    .nav-btn {
      padding: 10px 20px;
      border: none;
      background: var(--accent);
      color: white;
      border-radius: 25px;
      cursor: pointer;
      font-weight: 600;
      transition: all 0.3s ease;
    }

    .nav-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 5px 15px rgba(203, 91, 44, 0.3);
    }

    .nav-btn:disabled {
      background: var(--muted);
      cursor: not-allowed;
      opacity: 0.5;
    }

    .slide-counter {
      font-size: 0.9em;
      color: var(--muted);
      min-width: 60px;
      text-align: center;
    }

    .progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      height: 4px;
      background: var(--accent);
      transition: width 0.3s ease;
      z-index: 1001;
    }

    /* Tone classes for different slide types */
    .tone-danger { --accent: var(--danger); }
    .tone-warning { --accent: var(--warning); }
    .tone-success { --accent: var(--success); }

    .tone-danger h2 { color: var(--danger); }
    .tone-warning h2 { color: var(--warning); }
    .tone-success h2 { color: var(--success); }

    /* Responsive */
    @media (max-width: 768px) {
      .slide-content {
        padding: 30px;
      }

      h1 { font-size: 2em; }
      h2 { font-size: 1.5em; }

      .metrics-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <div class="progress-bar" id="progress-bar"></div>

  <div class="presentation-container">

    <!-- Slide 0: Title -->
    <section class="slide active" data-slide="0">
      <div class="slide-content">
        <h1>프리미엄 과일 커머스 전략</h1>
        <div class="subtitle">현실적 재평가 및 전환 전략 v3.0</div>
        <div class="warning-box">
          <h3>⚠️ Opus 4.1 종합 분석 결과</h3>
          <p><strong>현재 계획 성공률: 15%</strong></p>
          <p>즉시 전략 수정 필요 - 4개월 내 자금 고갈 위험</p>
        </div>
        <div class="metrics-grid">
          <div class="metric-card">
            <div class="metric-label">단위 경제성</div>
            <div class="metric-value">-9.6%</div>
            <div class="metric-change negative">판매 시 손실 발생</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">자본 부족</div>
            <div class="metric-value">122M원</div>
            <div class="metric-change negative">추가 자금 필요</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">손익분기</div>
            <div class="metric-value">19개월</div>
            <div class="metric-change negative">당초 7개월 → 19개월</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Slide 1: 핵심 문제 진단 -->
    <section class="slide tone-danger" data-slide="1">
      <div class="slide-content">
        <h2>🚨 치명적 문제 진단</h2>
        <div class="warning-box">
          <h3>1. 단위경제 실패</h3>
          <table>
            <tr>
              <th>항목</th>
              <th>계획</th>
              <th>실제</th>
              <th>차이</th>
            </tr>
            <tr>
              <td>샤인머스캣 2kg 판매가</td>
              <td>89,000원</td>
              <td>89,000원</td>
              <td>-</td>
            </tr>
            <tr>
              <td>총 비용</td>
              <td>80,000원</td>
              <td>97,500원</td>
              <td style="color: var(--danger)">+21.9%</td>
            </tr>
            <tr>
              <td>마진</td>
              <td>9,000원 (10.1%)</td>
              <td style="color: var(--danger)">-8,500원 (-9.6%)</td>
              <td style="color: var(--danger)">-17,500원</td>
            </tr>
          </table>

          <h3>2. 자본 계획 오류</h3>
          <ul>
            <li>필요 자본: 197.9M원</li>
            <li>계획 자본: 75.55M원</li>
            <li><strong style="color: var(--danger)">부족액: 122.35M원 (162% 부족)</strong></li>
          </ul>

          <h3>3. 고객획득비용 과소평가</h3>
          <ul>
            <li>예상 CAC: 14,200원</li>
            <li>실제 CAC: 28,000원</li>
            <li>LTV/CAC: 0.79 (1.0 미만으로 적자)</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Slide 2: 긴급 수정 계획 -->
    <section class="slide tone-warning" data-slide="2">
      <div class="slide-content">
        <h2>🔧 긴급 수정 계획 (Week 1-2)</h2>

        <div class="highlight">
          <h3>Phase 1: 생존 확보</h3>
          <table>
            <tr>
              <th>조치 항목</th>
              <th>현재</th>
              <th>수정</th>
              <th>기대 효과</th>
            </tr>
            <tr>
              <td>판매 가격</td>
              <td>89,000원</td>
              <td><strong>95,000원</strong></td>
              <td>마진 확보</td>
            </tr>
            <tr>
              <td>배송 전략</td>
              <td>개별 배송</td>
              <td><strong>권역별 묶음</strong></td>
              <td>-30% 비용</td>
            </tr>
            <tr>
              <td>포장재</td>
              <td>프리미엄</td>
              <td><strong>실용적 등급</strong></td>
              <td>-40% 비용</td>
            </tr>
            <tr>
              <td>마케팅</td>
              <td>광고 집행</td>
              <td><strong>일시 중단</strong></td>
              <td>현금 확보</td>
            </tr>
          </table>
        </div>

        <div class="metrics-grid">
          <div class="metric-card">
            <div class="metric-label">수정 후 마진</div>
            <div class="metric-value">5.2%</div>
            <div class="metric-change">흑자 전환</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">월 현금 소진</div>
            <div class="metric-value">18M → 9M</div>
            <div class="metric-change">50% 감소</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">생존 기간</div>
            <div class="metric-value">4개월 → 8개월</div>
            <div class="metric-change">2배 연장</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Slide 3: 피벗 전략 -->
    <section class="slide" data-slide="3">
      <div class="slide-content">
        <h2>🔄 전략적 피벗 - B2B + B2C 하이브리드</h2>

        <div class="success-box">
          <h3>새로운 수익 모델</h3>

          <div class="metrics-grid">
            <div class="metric-card">
              <div class="metric-label">B2B 기업 복지</div>
              <div class="metric-value">40%</div>
              <div class="metric-change">안정적 대량 주문</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">B2C 구독</div>
              <div class="metric-value">35%</div>
              <div class="metric-change">예측 가능한 수익</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">B2C 단건</div>
              <div class="metric-value">25%</div>
              <div class="metric-change">프리미엄 마진</div>
            </div>
          </div>
        </div>

        <table>
          <tr>
            <th>채널</th>
            <th>타겟</th>
            <th>단가</th>
            <th>마진율</th>
            <th>월 목표</th>
          </tr>
          <tr>
            <td><strong>B2B 기업복지</strong></td>
            <td>IT/금융사 100개</td>
            <td>75,000원</td>
            <td>8%</td>
            <td>200건</td>
          </tr>
          <tr>
            <td><strong>B2C 구독</strong></td>
            <td>월 2회 정기배송</td>
            <td>79,000원</td>
            <td>12%</td>
            <td>150명</td>
          </tr>
          <tr>
            <td><strong>B2C 프리미엄</strong></td>
            <td>선물/특별구매</td>
            <td>95,000원</td>
            <td>15%</td>
            <td>100건</td>
          </tr>
        </table>
      </div>
    </section>

    <!-- Slide 4: 자금 조달 계획 -->
    <section class="slide" data-slide="4">
      <div class="slide-content">
        <h2>💰 현실적 자금 조달 로드맵</h2>

        <div class="highlight">
          <h3>필요 자금: 200M원</h3>

          <table>
            <tr>
              <th>단계</th>
              <th>시기</th>
              <th>금액</th>
              <th>조달 방법</th>
              <th>용도</th>
            </tr>
            <tr>
              <td><strong>긴급</strong></td>
              <td>즉시</td>
              <td>50M</td>
              <td>창업자 추가 출자 / 가족</td>
              <td>운영자금</td>
            </tr>
            <tr>
              <td><strong>단기</strong></td>
              <td>1개월</td>
              <td>75M</td>
              <td>엔젤투자 / 크라우드펀딩</td>
              <td>재고+마케팅</td>
            </tr>
            <tr>
              <td><strong>중기</strong></td>
              <td>3개월</td>
              <td>75M</td>
              <td>정책자금 / TIPS</td>
              <td>시스템 구축</td>
            </tr>
          </table>

          <div class="warning-box">
            <p><strong>⚠️ 주의사항</strong></p>
            <ul>
              <li>현재 매출 실적 없이 투자 유치 어려움</li>
              <li>B2B 계약 확보 후 투자 접근 필요</li>
              <li>크라우드펀딩은 제품 검증 후 진행</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Slide 5: 수정된 목표 시장 -->
    <section class="slide" data-slide="5">
      <div class="slide-content">
        <h2>🎯 현실적 목표 시장 재정의</h2>

        <div class="metrics-grid">
          <div class="metric-card">
            <div class="metric-label">1차 타겟 (B2B)</div>
            <div class="metric-value">IT/금융 기업</div>
            <div class="metric-change">직원 복지 프로그램</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">2차 타겟 (B2C)</div>
            <div class="metric-value">35-45세 직장인</div>
            <div class="metric-change">가구 소득 8천만원+</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">3차 타겟</div>
            <div class="metric-value">선물 시장</div>
            <div class="metric-change">명절/기념일 특수</div>
          </div>
        </div>

        <table>
          <tr>
            <th>세그먼트</th>
            <th>시장 규모</th>
            <th>접근 전략</th>
            <th>예상 전환율</th>
          </tr>
          <tr>
            <td>대기업 복지</td>
            <td>500개 기업</td>
            <td>직접 영업</td>
            <td>5%</td>
          </tr>
          <tr>
            <td>스타트업</td>
            <td>1,000개</td>
            <td>샘플 제공</td>
            <td>10%</td>
          </tr>
          <tr>
            <td>프리미엄 가구</td>
            <td>50만 가구</td>
            <td>타겟 광고</td>
            <td>0.5%</td>
          </tr>
        </table>
      </div>
    </section>

    <!-- Slide 6: 운영 최적화 -->
    <section class="slide" data-slide="6">
      <div class="slide-content">
        <h2>⚙️ 운영 효율화 전략</h2>

        <div class="highlight">
          <h3>비용 구조 개선</h3>

          <table>
            <tr>
              <th>항목</th>
              <th>AS-IS</th>
              <th>TO-BE</th>
              <th>절감액</th>
            </tr>
            <tr>
              <td>원가 (2kg 기준)</td>
              <td>70,000원</td>
              <td>63,000원</td>
              <td>-10%</td>
            </tr>
            <tr>
              <td>물류비</td>
              <td>15,000원</td>
              <td>10,000원</td>
              <td>-33%</td>
            </tr>
            <tr>
              <td>포장비</td>
              <td>10,000원</td>
              <td>6,000원</td>
              <td>-40%</td>
            </tr>
            <tr>
              <td>마케팅비</td>
              <td>15,000원</td>
              <td>8,000원</td>
              <td>-47%</td>
            </tr>
            <tr style="background: rgba(16, 185, 129, 0.1);">
              <td><strong>총 비용</strong></td>
              <td><strong>110,000원</strong></td>
              <td><strong>87,000원</strong></td>
              <td><strong>-21%</strong></td>
            </tr>
          </table>
        </div>

        <div class="success-box">
          <h3>자동화 도입</h3>
          <ul>
            <li>주문 처리: Cafe24 + 네이버 스마트스토어 연동</li>
            <li>재고 관리: 실시간 동기화 시스템</li>
            <li>고객 응대: 챗봇 1차 대응 (70% 자동 처리)</li>
            <li>배송 최적화: 권역별 묶음 배송 자동 배정</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Slide 7: 제품 전략 수정 -->
    <section class="slide" data-slide="7">
      <div class="slide-content">
        <h2>🍇 제품 라인업 재구성</h2>

        <div class="metrics-grid">
          <div class="metric-card">
            <div class="metric-label">Hero 상품</div>
            <div class="metric-value">샤인머스캣</div>
            <div class="metric-change">시그니처 유지</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Volume 상품</div>
            <div class="metric-value">제철 과일 믹스</div>
            <div class="metric-change">마진 확보용</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Premium 상품</div>
            <div class="metric-value">한정 수입과일</div>
            <div class="metric-change">브랜드 포지셔닝</div>
          </div>
        </div>

        <table>
          <tr>
            <th>상품군</th>
            <th>SKU</th>
            <th>가격대</th>
            <th>마진율</th>
            <th>판매 비중</th>
          </tr>
          <tr>
            <td>샤인머스캣 플러스</td>
            <td>3 SKU</td>
            <td>79,000-119,000</td>
            <td>12%</td>
            <td>40%</td>
          </tr>
          <tr>
            <td>시즌 큐레이션</td>
            <td>4 SKU</td>
            <td>49,000-69,000</td>
            <td>18%</td>
            <td>35%</td>
          </tr>
          <tr>
            <td>프리미엄 선물세트</td>
            <td>2 SKU</td>
            <td>150,000-250,000</td>
            <td>25%</td>
            <td>10%</td>
          </tr>
          <tr>
            <td>기업 벌크</td>
            <td>2 SKU</td>
            <td>65,000-85,000</td>
            <td>8%</td>
            <td>15%</td>
          </tr>
        </table>
      </div>
    </section>

    <!-- Slide 8: 마케팅 전략 전환 -->
    <section class="slide" data-slide="8">
      <div class="slide-content">
        <h2>📣 저비용 고효율 마케팅</h2>

        <div class="highlight">
          <h3>퍼포먼스 마케팅 → 오가닉 성장</h3>

          <div class="metrics-grid">
            <div class="metric-card">
              <div class="metric-label">콘텐츠 마케팅</div>
              <div class="metric-value">40%</div>
              <div class="metric-change">블로그/유튜브</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">파트너십</div>
              <div class="metric-value">30%</div>
              <div class="metric-change">B2B 제휴</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">추천 프로그램</div>
              <div class="metric-value">20%</div>
              <div class="metric-change">고객 추천</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">유료 광고</div>
              <div class="metric-value">10%</div>
              <div class="metric-change">최소화</div>
            </div>
          </div>
        </div>

        <table>
          <tr>
            <th>채널</th>
            <th>월 예산</th>
            <th>목표 CAC</th>
            <th>예상 획득</th>
          </tr>
          <tr>
            <td>네이버 스마트스토어</td>
            <td>0원</td>
            <td>0원</td>
            <td>50명</td>
          </tr>
          <tr>
            <td>인스타그램 오가닉</td>
            <td>50만원</td>
            <td>10,000원</td>
            <td>50명</td>
          </tr>
          <tr>
            <td>B2B 직접영업</td>
            <td>100만원</td>
            <td>50,000원</td>
            <td>20개 기업</td>
          </tr>
          <tr>
            <td>고객 추천</td>
            <td>30만원</td>
            <td>6,000원</td>
            <td>50명</td>
          </tr>
        </table>
      </div>
    </section>

    <!-- Slide 9: 기술 스택 간소화 -->
    <section class="slide" data-slide="9">
      <div class="slide-content">
        <h2>💻 MVP 기술 스택</h2>

        <div class="success-box">
          <h3>빌드 vs 바이 결정</h3>

          <table>
            <tr>
              <th>기능</th>
              <th>초기 계획</th>
              <th>수정 계획</th>
              <th>절감 비용</th>
            </tr>
            <tr>
              <td>이커머스 플랫폼</td>
              <td>자체 개발</td>
              <td><strong>Cafe24</strong></td>
              <td>20M원</td>
            </tr>
            <tr>
              <td>결제 시스템</td>
              <td>PG 직접 연동</td>
              <td><strong>네이버페이</strong></td>
              <td>5M원</td>
            </tr>
            <tr>
              <td>CRM</td>
              <td>커스텀 개발</td>
              <td><strong>노션 + 구글시트</strong></td>
              <td>10M원</td>
            </tr>
            <tr>
              <td>물류 시스템</td>
              <td>WMS 구축</td>
              <td><strong>굿스플로</strong></td>
              <td>15M원</td>
            </tr>
          </table>
        </div>

        <div class="highlight">
          <h3>개발 우선순위</h3>
          <ol>
            <li><strong>Phase 1 (즉시):</strong> 기존 플랫폼 활용</li>
            <li><strong>Phase 2 (3개월):</strong> 자동화 스크립트</li>
            <li><strong>Phase 3 (6개월):</strong> 데이터 분석 도구</li>
            <li><strong>Phase 4 (12개월):</strong> 자체 플랫폼 검토</li>
          </ol>
        </div>
      </div>
    </section>

    <!-- Slide 10: 팀 구성 수정 -->
    <section class="slide" data-slide="10">
      <div class="slide-content">
        <h2>👥 현실적 팀 구성</h2>

        <div class="warning-box">
          <h3>창업자 번아웃 방지</h3>
          <p>1인 운영 불가능 - 최소 3명 필요</p>
        </div>

        <table>
          <tr>
            <th>역할</th>
            <th>시기</th>
            <th>고용 형태</th>
            <th>월 비용</th>
            <th>주요 업무</th>
          </tr>
          <tr>
            <td>창업자 (CEO)</td>
            <td>Day 1</td>
            <td>풀타임</td>
            <td>최소 생활비</td>
            <td>전략, 영업, 투자</td>
          </tr>
          <tr>
            <td>운영 매니저</td>
            <td>Month 1</td>
            <td>풀타임</td>
            <td>250만원</td>
            <td>CS, 물류, 구매</td>
          </tr>
          <tr>
            <td>마케터</td>
            <td>Month 2</td>
            <td>파트타임</td>
            <td>150만원</td>
            <td>콘텐츠, SNS</td>
          </tr>
          <tr>
            <td>개발자</td>
            <td>Month 6</td>
            <td>프리랜서</td>
            <td>프로젝트별</td>
            <td>자동화, 분석</td>
          </tr>
        </table>

        <div class="highlight">
          <h3>아웃소싱 활용</h3>
          <ul>
            <li>회계/세무: 월 30만원 대행</li>
            <li>디자인: 프로젝트별 외주</li>
            <li>물류: 3PL 위탁 (건당 과금)</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Slide 11: 리스크 관리 -->
    <section class="slide tone-warning" data-slide="11">
      <div class="slide-content">
        <h2>⚠️ 핵심 리스크 관리</h2>

        <table>
          <tr>
            <th>리스크</th>
            <th>발생 확률</th>
            <th>영향도</th>
            <th>대응 방안</th>
          </tr>
          <tr style="background: rgba(220, 38, 38, 0.1);">
            <td><strong>자금 고갈</strong></td>
            <td>높음 (80%)</td>
            <td>치명적</td>
            <td>즉시 추가 출자 + B2B 선금 확보</td>
          </tr>
          <tr style="background: rgba(245, 158, 11, 0.1);">
            <td><strong>품질 이슈</strong></td>
            <td>중간 (40%)</td>
            <td>높음</td>
            <td>다중 공급처 + 품질 보험</td>
          </tr>
          <tr>
            <td><strong>계절성</strong></td>
            <td>확실 (100%)</td>
            <td>중간</td>
            <td>다양한 제품군 + 수입과일</td>
          </tr>
          <tr>
            <td><strong>경쟁 심화</strong></td>
            <td>중간 (50%)</td>
            <td>중간</td>
            <td>B2B 락인 + 차별화</td>
          </tr>
          <tr>
            <td><strong>창업자 이탈</strong></td>
            <td>낮음 (20%)</td>
            <td>치명적</td>
            <td>팀 확장 + 권한 위임</td>
          </tr>
        </table>

        <div class="warning-box">
          <h3>생존 체크리스트</h3>
          <ul>
            <li>✅ 월 현금흐름 2개월분 확보</li>
            <li>✅ B2B 계약 최소 5개 확보</li>
            <li>✅ 단위경제 흑자 전환</li>
            <li>✅ 팀원 최소 2명 확보</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Slide 12: 수정된 재무 계획 -->
    <section class="slide" data-slide="12">
      <div class="slide-content">
        <h2>📊 현실적 재무 전망</h2>

        <table>
          <tr>
            <th>항목</th>
            <th>Month 1-3</th>
            <th>Month 4-6</th>
            <th>Month 7-12</th>
            <th>Year 2</th>
          </tr>
          <tr>
            <td>월 매출</td>
            <td>5M</td>
            <td>15M</td>
            <td>35M</td>
            <td>80M</td>
          </tr>
          <tr>
            <td>매출총이익률</td>
            <td>-5%</td>
            <td>5%</td>
            <td>12%</td>
            <td>18%</td>
          </tr>
          <tr>
            <td>운영비용</td>
            <td>15M</td>
            <td>18M</td>
            <td>25M</td>
            <td>35M</td>
          </tr>
          <tr style="background: rgba(220, 38, 38, 0.1);">
            <td>순이익</td>
            <td>-15.25M</td>
            <td>-17.25M</td>
            <td>-20.8M</td>
            <td>-20.6M</td>
          </tr>
          <tr>
            <td>누적 투자 필요</td>
            <td>45M</td>
            <td>97M</td>
            <td>222M</td>
            <td>470M</td>
          </tr>
        </table>

        <div class="highlight">
          <h3>손익분기점</h3>
          <ul>
            <li><strong>낙관적:</strong> 18개월 (B2B 성공 시)</li>
            <li><strong>현실적:</strong> 24개월</li>
            <li><strong>비관적:</strong> 36개월+</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Slide 13: KPI 재설정 -->
    <section class="slide" data-slide="13">
      <div class="slide-content">
        <h2>📈 핵심 KPI 재설정</h2>

        <div class="metrics-grid">
          <div class="metric-card">
            <div class="metric-label">생존 지표</div>
            <div class="metric-value">Runway</div>
            <div class="metric-change">최소 6개월 유지</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">수익성 지표</div>
            <div class="metric-value">Unit Economics</div>
            <div class="metric-change">마진 10% 이상</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">성장 지표</div>
            <div class="metric-value">MRR</div>
            <div class="metric-change">월 20% 성장</div>
          </div>
        </div>

        <table>
          <tr>
            <th>KPI</th>
            <th>Month 3</th>
            <th>Month 6</th>
            <th>Month 12</th>
            <th>측정 방법</th>
          </tr>
          <tr>
            <td>월 매출 (MRR)</td>
            <td>10M</td>
            <td>25M</td>
            <td>50M</td>
            <td>구독 + 반복구매</td>
          </tr>
          <tr>
            <td>고객 수</td>
            <td>100</td>
            <td>300</td>
            <td>800</td>
            <td>유니크 구매자</td>
          </tr>
          <tr>
            <td>B2B 계약</td>
            <td>5</td>
            <td>15</td>
            <td>40</td>
            <td>활성 계약 수</td>
          </tr>
          <tr>
            <td>재구매율</td>
            <td>20%</td>
            <td>35%</td>
            <td>50%</td>
            <td>3개월 내 재구매</td>
          </tr>
          <tr>
            <td>CAC/LTV</td>
            <td>2.0</td>
            <td>1.5</td>
            <td>0.8</td>
            <td>6개월 LTV 기준</td>
          </tr>
        </table>
      </div>
    </section>

    <!-- Slide 14: 실행 타임라인 -->
    <section class="slide" data-slide="14">
      <div class="slide-content">
        <h2>📅 90일 실행 로드맵</h2>

        <div class="highlight">
          <h3>🚨 Week 1-2: 긴급 조치</h3>
          <ul>
            <li>✅ 가격 인상 (89,000 → 95,000)</li>
            <li>✅ 마케팅 비용 중단</li>
            <li>✅ 포장재 다운그레이드</li>
            <li>✅ 창업자 추가 출자</li>
          </ul>

          <h3>💼 Week 3-4: B2B 영업</h3>
          <ul>
            <li>타겟 기업 100개 리스트업</li>
            <li>샘플 제작 및 발송</li>
            <li>제안서 커스터마이징</li>
            <li>미팅 일정 확보</li>
          </ul>

          <h3>🛒 Month 2: 플랫폼 구축</h3>
          <ul>
            <li>Cafe24 스토어 오픈</li>
            <li>네이버 스마트스토어 등록</li>
            <li>구독 상품 페이지 제작</li>
            <li>자동화 프로세스 구축</li>
          </ul>

          <h3>📊 Month 3: 최적화</h3>
          <ul>
            <li>데이터 분석 체계 구축</li>
            <li>고객 피드백 반영</li>
            <li>공급망 최적화</li>
            <li>시리즈 A 준비</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Slide 15: Go/No-Go 의사결정 -->
    <section class="slide tone-danger" data-slide="15">
      <div class="slide-content">
        <h2>🚦 Go/No-Go 체크포인트</h2>

        <div class="warning-box">
          <h3>Month 3 평가 기준</h3>

          <table>
            <tr>
              <th>항목</th>
              <th>Go 기준</th>
              <th>현재 전망</th>
              <th>판단</th>
            </tr>
            <tr>
              <td>월 매출</td>
              <td>15M 이상</td>
              <td>10M</td>
              <td style="color: var(--warning);">⚠️ 주의</td>
            </tr>
            <tr>
              <td>B2B 계약</td>
              <td>5개 이상</td>
              <td>미확정</td>
              <td style="color: var(--warning);">⚠️ 주의</td>
            </tr>
            <tr>
              <td>단위 경제</td>
              <td>흑자 전환</td>
              <td>5% 예상</td>
              <td style="color: var(--success);">✅ 가능</td>
            </tr>
            <tr>
              <td>추가 자금</td>
              <td>50M 확보</td>
              <td>미확정</td>
              <td style="color: var(--danger);">❌ 위험</td>
            </tr>
            <tr>
              <td>팀 구성</td>
              <td>3명 이상</td>
              <td>1명</td>
              <td style="color: var(--danger);">❌ 위험</td>
            </tr>
          </table>
        </div>

        <div class="highlight">
          <h3>피벗 또는 중단 시그널</h3>
          <ul>
            <li>3개월 내 B2B 계약 0건</li>
            <li>월 burn rate > 30M</li>
            <li>추가 자금 조달 실패</li>
            <li>창업자 건강 문제</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Slide 16: 결론 및 제언 -->
    <section class="slide" data-slide="16">
      <div class="slide-content">
        <h2>💡 최종 제언</h2>

        <div class="highlight">
          <h3>Opus 4.1 종합 평가</h3>
          <div style="font-size: 1.5em; text-align: center; margin: 30px 0;">
            <strong>"아이디어 A급, 실행 계획 C급"</strong>
          </div>
        </div>

        <div class="metrics-grid">
          <div class="metric-card">
            <div class="metric-label">현재 계획 성공률</div>
            <div class="metric-value" style="color: var(--danger);">15%</div>
            <div class="metric-change negative">즉시 수정 필요</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">수정 후 성공률</div>
            <div class="metric-value" style="color: var(--warning);">45%</div>
            <div class="metric-change">조건부 진행 가능</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">최적화 후</div>
            <div class="metric-value" style="color: var(--success);">65%</div>
            <div class="metric-change">투자 가능 수준</div>
          </div>
        </div>

        <div class="warning-box">
          <h3>🔴 즉시 실행 필수 사항</h3>
          <ol>
            <li><strong>자금 확보:</strong> 최소 50M 즉시 조달</li>
            <li><strong>가격 조정:</strong> 95,000원으로 인상</li>
            <li><strong>B2B 피벗:</strong> 기업 영업 즉시 시작</li>
            <li><strong>팀 확장:</strong> 운영 매니저 긴급 채용</li>
            <li><strong>비용 절감:</strong> 모든 불필요 지출 중단</li>
          </ol>
        </div>

        <div class="success-box">
          <h3>성공 가능 시나리오</h3>
          <p>B2B 중심 피벗 + 구독 모델 + 150M 추가 자금 확보 시</p>
          <p><strong>24개월 내 손익분기 가능</strong></p>
        </div>
      </div>
    </section>

  </div>

  <!-- Navigation -->
  <div class="navigation">
    <button class="nav-btn" id="prev-btn">이전</button>
    <div class="slide-counter">
      <span id="current-slide">1</span> / <span id="total-slides">17</span>
    </div>
    <button class="nav-btn" id="next-btn">다음</button>
  </div>

  <script>
    let currentSlideIndex = 0;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;

    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const currentSlideSpan = document.getElementById('current-slide');
    const totalSlidesSpan = document.getElementById('total-slides');
    const progressBar = document.getElementById('progress-bar');

    totalSlidesSpan.textContent = totalSlides;

    function showSlide(index) {
      // Boundary checks
      if (index < 0) index = 0;
      if (index >= totalSlides) index = totalSlides - 1;

      // Update slide visibility
      slides.forEach((slide, i) => {
        slide.classList.remove('active', 'prev');
        if (i < index) {
          slide.classList.add('prev');
        } else if (i === index) {
          slide.classList.add('active');
        }
      });

      currentSlideIndex = index;

      // Update UI
      currentSlideSpan.textContent = index + 1;
      prevBtn.disabled = index === 0;
      nextBtn.disabled = index === totalSlides - 1;

      // Update progress bar
      const progress = ((index + 1) / totalSlides) * 100;
      progressBar.style.width = progress + '%';
    }

    // Event listeners
    prevBtn.addEventListener('click', () => {
      showSlide(currentSlideIndex - 1);
    });

    nextBtn.addEventListener('click', () => {
      showSlide(currentSlideIndex + 1);
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') {
        showSlide(currentSlideIndex - 1);
      } else if (e.key === 'ArrowRight') {
        showSlide(currentSlideIndex + 1);
      } else if (e.key === 'Home') {
        showSlide(0);
      } else if (e.key === 'End') {
        showSlide(totalSlides - 1);
      }
    });

    // Touch/swipe support for mobile
    let touchStartX = 0;
    let touchEndX = 0;

    document.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    });

    document.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    });

    function handleSwipe() {
      if (touchEndX < touchStartX - 50) {
        // Swipe left - next slide
        showSlide(currentSlideIndex + 1);
      }
      if (touchEndX > touchStartX + 50) {
        // Swipe right - previous slide
        showSlide(currentSlideIndex - 1);
      }
    }

    // Initialize
    showSlide(0);
  </script>
</body>
</html>'''

    # Save the file
    output_path = 'C:/Users/dkskr/OneDrive/111/fruits/output/strategy_proposal_comprehensive_revised.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("SUCCESS: Comprehensive revised presentation created!")
    print(f"File location: {output_path}")
    print("Total slides: 17")
    print("Opus analysis findings fully integrated")
    return output_path

if __name__ == "__main__":
    create_revised_presentation()