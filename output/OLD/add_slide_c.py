#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# v2 파일 읽기
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 슬라이드 C: 경쟁사 포지셔닝 (슬라이드 #10 다음, 현재 슬라이드 #11 앞에 삽입)
# data-slide-index="11"을 찾아서 그 앞에 삽입
new_slide_c = '''      <section class="slide tone-4" data-slide-index="11" data-chapter="3">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">차별화</span>
            <strong>15 / 29</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Competitive Positioning</div>
                  <h2 class="title">경쟁 포지셔닝 - 과일 전문성과 듀얼 모델로 차별화합니다</h2>
                  <div class="desc">종합 신선식품 플랫폼들과 달리, 우리는 과일 100% 전문화와 B2B+B2C 듀얼 모델로 Blue Ocean 영역을 확보합니다.</div>
                </div>
                <div class="pill">Blue Ocean via Specialization</div>
              </div>
              <div class="board">
                <div class="chart">
                  <h3>주요 경쟁사 비교</h3>
                  <p>2024년 기준 신선식품 온라인 플랫폼의 전략적 포지셔닝 분석입니다.</p>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>구분</th>
                        <th>마켓컬리</th>
                        <th>오아시스마켓</th>
                        <th>쿠팡 로켓프레시</th>
                        <th><strong>우리 (전략 A)</strong></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>2024 매출</td>
                        <td>2조 1,956억 (+6%)</td>
                        <td>5,171억 (+9%)</td>
                        <td>비공개</td>
                        <td>-</td>
                      </tr>
                      <tr>
                        <td>핵심 전략</td>
                        <td>프리미엄 큐레이션</td>
                        <td>착한가격+유기농</td>
                        <td>산지직송+최저가</td>
                        <td><strong>과일 전문 큐레이션</strong></td>
                      </tr>
                      <tr>
                        <td>과일 비중</td>
                        <td>전체의 ~20%</td>
                        <td>전체의 ~15%</td>
                        <td>전체의 ~10%</td>
                        <td><strong>100% (특화)</strong></td>
                      </tr>
                      <tr>
                        <td>B2B 모델</td>
                        <td>없음</td>
                        <td>없음</td>
                        <td>없음</td>
                        <td><strong>도매 연계</strong></td>
                      </tr>
                      <tr>
                        <td>차별점</td>
                        <td>새벽배송+뷰티</td>
                        <td>13년 연속 흑자</td>
                        <td>압도적 물류</td>
                        <td><strong>결정 대행 UX</strong></td>
                      </tr>
                      <tr>
                        <td>약점</td>
                        <td>가격 높음</td>
                        <td>배송 지역 제한</td>
                        <td>전문성 부족</td>
                        <td>브랜드 인지도 제로</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="chart">
                  <h3>Blue Ocean 기회 영역</h3>
                  <p>종합 플랫폼이 놓치고 있는 4가지 전략적 기회입니다.</p>
                  <div class="grid-2">
                    <article class="card">
                      <h3>과일 전문 플랫폼</h3>
                      <p>컬리/오아시스/쿠팡은 과일이 전체의 10~20%. 우리는 100% 과일 전문으로 깊이 있는 큐레이션과 상황별 추천 가능.</p>
                    </article>
                    <article class="card">
                      <h3>B2B+B2C 듀얼 모델</h3>
                      <p>경쟁사는 소매만 운영. 우리는 도매 Cash Cow로 원가 경쟁력 확보 + B2C로 신시장 개척.</p>
                    </article>
                    <article class="card">
                      <h3>결정 대행 UX</h3>
                      <p>경쟁사는 당도/가격 경쟁. 우리는 "지금 이 상황에 어떤 과일이 맞는가"를 대신 골라주는 서비스.</p>
                    </article>
                    <article class="card">
                      <h3>제철 큐레이션</h3>
                      <p>계절별 최적 품종 제안으로 자연스러운 재방문 유도. 일회성 할인이 아닌 루틴 설계.</p>
                    </article>
                  </div>
                </div>
              </div>
              <div style="margin-top:32px; padding-top:16px; border-top:1px solid var(--line); font-size:11px; color:var(--muted)">
                <p style="margin:4px 0">[1] 매출 데이터: 각사 공시자료 및 언론 보도 (2024년 기준)</p>
                <p style="margin:4px 0">[2] 과일 비중: research/competitor_analysis.md 분석 기반 추정</p>
              </div>
            </div>
          </section>
        </div>
      </section>
      '''

# 기존 슬라이드 11 (data-slide-index="11") 앞에 삽입
# 패턴: 슬라이드 10이 끝나고 슬라이드 11이 시작하는 지점
pattern = r'(      </section>\n      <section class="slide tone-4" data-slide-index="11")'
modified_content = re.sub(pattern, new_slide_c + r'<section class="slide tone-4" data-slide-index="12"', content, count=1)

# 이후 모든 data-slide-index를 2개씩 증가 (11→12, 12→13, ..., 17→19)
# 슬라이드 12부터 19까지 순차 증가
for old_idx in range(18, 11, -1):  # 18부터 12까지 역순으로
    new_idx = old_idx + 1
    modified_content = re.sub(
        f'data-slide-index="{old_idx}"',
        f'data-slide-index="{new_idx}"',
        modified_content
    )

# 저장
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'w', encoding='utf-8') as f:
    f.write(modified_content)

print("Done: Added Slide C (Competitive Positioning)")
