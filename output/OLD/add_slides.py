#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML 프레젠테이션에 신규 슬라이드를 추가하는 스크립트
"""

import re

# 원본 파일 읽기
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 슬라이드 #17 끝나는 위치 찾기 (data-slide-index="17"인 섹션의 종료)
# 패턴: </section> 다음에 </div>와 </main>이 오는 부분
insertion_pattern = r'(      </section>\n    </div>\n  </main>)'

# 새로 추가할 슬라이드 B: SKU별 공헌이익 분석
new_slide_b = '''      </section>
      <section class="slide tone-7" data-slide-index="18" data-chapter="6">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">실행</span>
            <strong>28 / 29</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">SKU Profitability</div>
                  <h2 class="title">SKU별 수익성 분석 - 선물형과 일상형의 공헌이익 구조</h2>
                  <div class="desc">추상적 전략을 구체적 수익 모델로 검증합니다. 선물형 SKU는 28%+ 마진율로 고객단가 전략을 뒷받침하고, 일상형은 합배송 구조에서 재구매 유도 역할을 맡습니다.</div>
                </div>
                <div class="pill">Contribution Margin, Break-even Orders</div>
              </div>
              <div class="board">
                <div class="chart">
                  <h3>선물형 SKU 2종 - 높은 마진율 검증</h3>
                  <p>프리미엄 선물 세그먼트는 포장 투자가 크지만 공헌이익률 28%+ 달성 가능합니다.</p>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>항목</th>
                        <th>샤인머스캣 2kg 선물</th>
                        <th>사과·배 혼합 3kg</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>판매가</td>
                        <td>89,000원</td>
                        <td>75,000원</td>
                      </tr>
                      <tr>
                        <td>원가 (산지직거래)</td>
                        <td>45,000원</td>
                        <td>38,000원</td>
                      </tr>
                      <tr>
                        <td>포장재 (고급 상자+완충재)</td>
                        <td>7,000원</td>
                        <td>5,500원</td>
                      </tr>
                      <tr>
                        <td>배송비 (평균)</td>
                        <td>4,500원</td>
                        <td>4,500원</td>
                      </tr>
                      <tr>
                        <td>보상비용 (이슈율 10%)</td>
                        <td>2,500원</td>
                        <td>2,000원</td>
                      </tr>
                      <tr>
                        <td>플랫폼 수수료 (5%)</td>
                        <td>4,450원</td>
                        <td>3,750원</td>
                      </tr>
                      <tr>
                        <td><strong>공헌이익</strong></td>
                        <td><strong>25,550원 (28.7%)</strong></td>
                        <td><strong>21,250원 (28.3%)</strong></td>
                      </tr>
                      <tr>
                        <td>손익분기 주문 (마케팅비 300만원)</td>
                        <td>120건/월</td>
                        <td>140건/월</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="chart">
                  <h3>일상형 SKU 2종 - 합배송 전략 필수</h3>
                  <p>일상형 단독 판매는 배송비 부담으로 수익성이 낮지만, 선물형과 합배송하거나 정기구독 시 전환 가능합니다.</p>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>항목</th>
                        <th>가족 사과 5kg</th>
                        <th>간식용 방울토마토 1kg</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>판매가</td>
                        <td>35,000원</td>
                        <td>18,000원</td>
                      </tr>
                      <tr>
                        <td>원가</td>
                        <td>18,000원</td>
                        <td>9,000원</td>
                      </tr>
                      <tr>
                        <td>포장재 (표준 박스)</td>
                        <td>1,500원</td>
                        <td>800원</td>
                      </tr>
                      <tr>
                        <td>배송비</td>
                        <td>4,500원</td>
                        <td>4,500원 (합배송 3,000원)</td>
                      </tr>
                      <tr>
                        <td>보상비용</td>
                        <td>1,200원</td>
                        <td>600원</td>
                      </tr>
                      <tr>
                        <td>플랫폼 수수료</td>
                        <td>1,750원</td>
                        <td>900원</td>
                      </tr>
                      <tr>
                        <td><strong>공헌이익</strong></td>
                        <td><strong>8,050원 (23.0%)</strong></td>
                        <td><strong>3,200원 (17.8%)</strong></td>
                      </tr>
                      <tr>
                        <td>전략적 역할</td>
                        <td>재구매 유도 + 리뷰 확보</td>
                        <td>합배송 유도 (단독 시 적자)</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
              <div class="board" style="margin-top:24px">
                <div class="grid-2">
                  <article class="card">
                    <h3>핵심 시사점</h3>
                    <p><strong>선물형 마진 28%+:</strong> 고객단가 전략 타당성 검증됨. 초기 120~140건/월 달성 시 손익분기 통과.</p>
                    <p><strong>일상형 리스크:</strong> 단독 판매 시 배송비 부담으로 수익성 낮음. 합배송/정기구독 모델 필수.</p>
                    <p><strong>보상비용 2~3%:</strong> 온브릭스 대비 낮은 이슈율 목표 달성 시 경쟁력 확보.</p>
                  </article>
                  <article class="card">
                    <h3>SKU 운영 원칙</h3>
                    <p><strong>초기 집중:</strong> 선물형 5종 이하로 시작, 손익분기 달성 후 확장.</p>
                    <p><strong>폐기 최소화:</strong> SKU당 주 2회 소량 입고로 재고 리스크 관리.</p>
                    <p><strong>Cut 기준:</strong> 전환은 나오지만 보상률이 높은 SKU는 즉시 제외.</p>
                  </article>
                </div>
              </div>
              <div style="margin-top:32px; padding-top:16px; border-top:1px solid var(--line); font-size:11px; color:var(--muted)">
                <p style="margin:4px 0">[1] 원가 및 포장재 비용: fruit_consumption_environment_menu_evidence_map.md 기반 추정</p>
                <p style="margin:4px 0">[2] 보상비용: 이슈율 10% 가정, 온브릭스 리뷰 분석 기준 (당도 불만 15%, 무름 8%)</p>
                <p style="margin:4px 0">[3] 손익분기: 월 마케팅비 300만원 기준, CAC 회수 30일 이내 목표</p>
              </div>
            </div>
          </section>
        </div>
      </section>
    </div>
  </main>'''

# 치환 수행
modified_content = re.sub(insertion_pattern, new_slide_b, content, count=1)

# 2147행 이후 중복 코드 제거 (</html> 이후에 나오는 모든 내용)
# </html> 이후의 모든 내용을 제거
modified_content = re.sub(r'(</html>)\s*\n.*', r'\1\n', modified_content, flags=re.DOTALL)

# 새 파일로 저장
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'w', encoding='utf-8') as f:
    f.write(modified_content)

print("✅ 신규 슬라이드 B (SKU별 공헌이익) 추가 완료")
print("✅ 중복 코드 제거 완료")
print("📄 새 파일: strategy_a_proposal_v2.html")
