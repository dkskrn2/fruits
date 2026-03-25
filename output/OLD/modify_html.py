#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
import io

# UTF-8 출력 설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 원본 파일 읽기
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 슬라이드 B 추가
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
                        <td>손익분기 주문</td>
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
                        <td>포장재</td>
                        <td>1,500원</td>
                        <td>800원</td>
                      </tr>
                      <tr>
                        <td>배송비</td>
                        <td>4,500원</td>
                        <td>4,500원</td>
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
                        <td>재구매 유도</td>
                        <td>합배송 유도</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
              <div class="board" style="margin-top:24px">
                <div class="grid-2">
                  <article class="card">
                    <h3>핵심 시사점</h3>
                    <p><strong>선물형 마진 28%+:</strong> 고객단가 전략 타당성 검증됨.</p>
                    <p><strong>일상형 리스크:</strong> 합배송/정기구독 모델 필수.</p>
                  </article>
                  <article class="card">
                    <h3>SKU 운영 원칙</h3>
                    <p><strong>초기 집중:</strong> 선물형 5종 이하로 시작.</p>
                    <p><strong>폐기 최소화:</strong> SKU당 주 2회 소량 입고.</p>
                  </article>
                </div>
              </div>
              <div style="margin-top:32px; padding-top:16px; border-top:1px solid var(--line); font-size:11px; color:var(--muted)">
                <p style="margin:4px 0">[1] 원가: fruit_consumption_environment_menu_evidence_map.md 기반 추정</p>
                <p style="margin:4px 0">[2] 보상비용: 이슈율 10% 가정 (온브릭스 당도 불만 15%, 무름 8%)</p>
              </div>
            </div>
          </section>
        </div>
      </section>
    </div>
  </main>'''

# 패턴 찾아서 치환
pattern = r'(      </section>\n    </div>\n  </main>)'
modified_content = re.sub(pattern, new_slide_b, content, count=1)

# 중복 코드 제거
modified_content = re.sub(r'(</html>)\s*\n.*', r'\1\n', modified_content, flags=re.DOTALL)

# 저장
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'w', encoding='utf-8') as f:
    f.write(modified_content)

print("Done: strategy_a_proposal_v2.html")
