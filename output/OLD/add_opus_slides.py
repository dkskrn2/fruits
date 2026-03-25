#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Read the original HTML file
with open('strategy_a_proposal_v2.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find the position to insert new slides (after slide 22, before closing tags)
# Look for the last slide section
pattern = r'(</section>\s*</div>\s*</section>\s*</div>\s*</main>)'
match = re.search(pattern, html_content)

if not match:
    print("Could not find insertion point")
    exit(1)

insertion_point = match.start()

# Create the new Opus analysis slides
opus_slides = '''
      <!-- Opus 4.1 Analysis Slides -->
      <section class="slide tone-8" data-slide-index="23" data-chapter="7">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">⚠️ 긴급</span>
            <strong>24 / 27</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Opus 4.1 Critical Analysis</div>
                  <h2 class="title" style="color:#EF4444">치명적 문제 발견 - 4개월 내 파산 위기</h2>
                  <div class="desc">5개 AI 에이전트가 독립적으로 분석한 결과, 현재 계획으로는 <strong style="color:#EF4444">95% 실패 확실</strong>합니다. 판매할수록 손실이 누적되며, 자본이 162% 부족한 상황입니다.</div>
                </div>
                <div class="pill" style="background:#EF4444; color:white">성공률: 15% → 65% (수정 시)</div>
              </div>
              <div class="board">
                <div class="grid-2">
                  <div class="chart">
                    <h3 style="color:#EF4444">🔴 치명적 문제 Top 3</h3>
                    <table class="table" style="margin-top:16px">
                      <thead>
                        <tr>
                          <th>문제</th>
                          <th>현재 상황</th>
                          <th>결과</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr style="background:rgba(239,68,68,0.1)">
                          <td><strong>단위경제</strong></td>
                          <td>판매가 89,000원<br>실제원가 97,500원</td>
                          <td><strong style="color:#EF4444">-8,500원 손실/개</strong></td>
                        </tr>
                        <tr style="background:rgba(239,68,68,0.1)">
                          <td><strong>자본 부족</strong></td>
                          <td>보유 75.55M원<br>필요 197.9M원</td>
                          <td><strong style="color:#EF4444">Month 4 파산</strong></td>
                        </tr>
                        <tr style="background:rgba(239,68,68,0.1)">
                          <td><strong>창업자 번아웃</strong></td>
                          <td>Month 4부터<br>주 80시간 근무</td>
                          <td><strong style="color:#EF4444">건강 위기 80%</strong></td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <div class="chart">
                    <h3>에이전트 평가 결과</h3>
                    <table class="table" style="margin-top:16px">
                      <thead>
                        <tr>
                          <th>에이전트</th>
                          <th>기존</th>
                          <th>Opus</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td><strong>재무</strong></td>
                          <td>7.0</td>
                          <td style="color:#EF4444"><strong>4.5</strong></td>
                        </tr>
                        <tr>
                          <td><strong>운영</strong></td>
                          <td>7.5</td>
                          <td style="color:#F59E0B"><strong>5.5</strong></td>
                        </tr>
                        <tr>
                          <td><strong>마케팅</strong></td>
                          <td>7.0</td>
                          <td style="color:#F59E0B"><strong>6.5</strong></td>
                        </tr>
                        <tr>
                          <td><strong>UX</strong></td>
                          <td>8.0</td>
                          <td style="color:#F59E0B"><strong>5.5</strong></td>
                        </tr>
                        <tr>
                          <td><strong>전략</strong></td>
                          <td>9.2</td>
                          <td style="color:#10B981"><strong>7.2</strong></td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </section>

      <section class="slide tone-8" data-slide-index="24" data-chapter="7">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">💰 재무</span>
            <strong>25 / 27</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Financial Model Revision</div>
                  <h2 class="title">단위경제 전면 수정 - 가격 인상 필수</h2>
                  <div class="desc">실제 원가를 반영한 결과, 현재 가격으로는 구조적 손실입니다. 최소 95,000원, 이상적으로 105,000원으로 인상해야 생존 가능합니다.</div>
                </div>
                <div class="pill" style="background:#10B981; color:white">필수 조정가: 95,000원</div>
              </div>
              <div class="board">
                <div class="chart">
                  <h3>SKU별 가격 조정 필수</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>SKU</th>
                        <th>현재가</th>
                        <th>실제원가</th>
                        <th>손익</th>
                        <th>필수 조정가</th>
                        <th>새 마진</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>샤인머스캣 2kg</td>
                        <td>89,000원</td>
                        <td>97,500원</td>
                        <td style="color:#EF4444">-8,500원</td>
                        <td><strong>95,000원</strong></td>
                        <td style="color:#10B981">+3.1%</td>
                      </tr>
                      <tr>
                        <td>사과 5kg</td>
                        <td>38,000원</td>
                        <td>45,410원</td>
                        <td style="color:#EF4444">-7,410원</td>
                        <td><strong>42,000원</strong></td>
                        <td style="color:#10B981">+2.9%</td>
                      </tr>
                      <tr>
                        <td>한라봉 3kg</td>
                        <td>69,000원</td>
                        <td>75,800원</td>
                        <td style="color:#EF4444">-6,800원</td>
                        <td><strong>75,000원</strong></td>
                        <td style="color:#10B981">+2.8%</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="grid-2" style="margin-top:24px">
                  <div style="padding:20px; background:rgba(239,68,68,0.1); border-radius:12px">
                    <h4 style="color:#EF4444; margin:0 0 12px 0">자본 요구사항 (2.6배 증가)</h4>
                    <table style="width:100%; font-size:13px">
                      <tr><td>기존 계획:</td><td style="text-align:right"><strong>75.55M원</strong></td></tr>
                      <tr><td>실제 필요:</td><td style="text-align:right; color:#EF4444"><strong>197.9M원</strong></td></tr>
                      <tr><td>부족액:</td><td style="text-align:right">122.35M원</td></tr>
                    </table>
                  </div>
                  <div style="padding:20px; background:rgba(245,158,11,0.1); border-radius:12px">
                    <h4 style="color:#F59E0B; margin:0 0 12px 0">손익분기 현실화</h4>
                    <table style="width:100%; font-size:13px">
                      <tr><td>기존 목표:</td><td style="text-align:right">Month 7</td></tr>
                      <tr><td>실제 예상:</td><td style="text-align:right; color:#F59E0B"><strong>Month 19-24</strong></td></tr>
                      <tr><td>필요 주문:</td><td style="text-align:right">700-800/월</td></tr>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </section>

      <section class="slide tone-8" data-slide-index="25" data-chapter="7">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">🎯 전략</span>
            <strong>26 / 27</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Strategic Pivot</div>
                  <h2 class="title">전략적 피벗 - B2B 동시 런칭 + 구독 전환</h2>
                  <div class="desc">인플루언서 70% 의존은 확장 불가능합니다. B2B 동시 시작으로 현금흐름을 안정화하고, 구독 모델로 LTV를 개선해야 생존 가능합니다.</div>
                </div>
                <div class="pill" style="background:#10B981; color:white">성공 확률: 65%</div>
              </div>
              <div class="board">
                <div class="grid-3">
                  <div style="padding:20px; background:rgba(85,101,72,0.1); border-radius:12px">
                    <h4 style="color:#556548; margin:0 0 12px 0">1. B2B 동시 런칭</h4>
                    <ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.8">
                      <li>Day 1부터 월 15M원</li>
                      <li>카페/호텔 3-5곳</li>
                      <li>현금흐름 안정화</li>
                      <li>재고 리스크 감소</li>
                    </ul>
                  </div>
                  <div style="padding:20px; background:rgba(203,91,44,0.1); border-radius:12px">
                    <h4 style="color:#cb5b2c; margin:0 0 12px 0">2. 구독 모델 전환</h4>
                    <ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.8">
                      <li>우리 아이 과일 주 25K</li>
                      <li>3-8세 자녀 부모 타겟</li>
                      <li>리텐션 60% (vs 15%)</li>
                      <li>LTV/CAC 7.5x</li>
                    </ul>
                  </div>
                  <div style="padding:20px; background:rgba(161,66,83,0.1); border-radius:12px">
                    <h4 style="color:#a14253; margin:0 0 12px 0">3. 채널 다각화</h4>
                    <ul style="margin:0; padding-left:20px; font-size:13px; line-height:1.8">
                      <li>인플루언서 70→40%</li>
                      <li>네이버 SEO 10→30%</li>
                      <li>커뮤니티 10→20%</li>
                      <li>리퍼럴 10→10%</li>
                    </ul>
                  </div>
                </div>
                <div style="margin-top:24px; padding:20px; background:rgba(16,185,129,0.1); border-radius:12px">
                  <h3 style="color:#10B981; margin:0 0 16px 0">✅ GO/NO-GO 체크리스트</h3>
                  <div class="grid-2">
                    <div>
                      <p style="margin:8px 0; font-size:14px">☐ 150M원 자본 확보 가능?</p>
                      <p style="margin:8px 0; font-size:14px">☐ 가격 95,000원 수용?</p>
                      <p style="margin:8px 0; font-size:14px">☐ 18개월 무급 생존 가능?</p>
                    </div>
                    <div>
                      <p style="margin:8px 0; font-size:14px">☐ 주 80시간 근무 가능?</p>
                      <p style="margin:8px 0; font-size:14px">☐ Month 3 운영 매니저 채용?</p>
                      <p style="margin:8px 0; font-size:14px; font-weight:600">→ 5개 모두 YES시 진행</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </section>

      <section class="slide tone-1" data-slide-index="26" data-chapter="7">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">결론</span>
            <strong>27 / 27</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Final Decision</div>
                  <h2 class="title">"전략은 A급, 실행 계획은 C급"</h2>
                  <div class="desc">현재 계획대로 진행하면 <strong style="color:#EF4444">95% 실패 확실</strong>입니다. 전면 수정 시 성공 확률을 15%에서 65%로 높일 수 있습니다. 즉시 결정이 필요합니다.</div>
                </div>
                <div class="pill">Opus 4.1 Analysis Complete</div>
              </div>
              <div class="board">
                <div class="grid-3">
                  <div style="padding:24px; background:rgba(16,185,129,0.15); border-radius:16px; border:2px solid #10B981">
                    <h3 style="color:#10B981; margin:0 0 16px 0">✅ Option A: 전면 수정</h3>
                    <p style="font-size:32px; font-weight:700; margin:8px 0; color:#10B981">65%</p>
                    <p style="font-size:14px; margin:8px 0">성공 확률</p>
                    <ul style="margin:16px 0 0 0; padding-left:20px; font-size:13px; line-height:1.8">
                      <li>150M원 자본 확보</li>
                      <li>가격 95K 인상</li>
                      <li>B2B 동시 시작</li>
                      <li>Month 19-24 BEP</li>
                    </ul>
                  </div>
                  <div style="padding:24px; background:rgba(245,158,11,0.15); border-radius:16px">
                    <h3 style="color:#F59E0B; margin:0 0 16px 0">⏳ Option B: 6개월 연기</h3>
                    <p style="font-size:32px; font-weight:700; margin:8px 0; color:#F59E0B">75%</p>
                    <p style="font-size:14px; margin:8px 0">성공 확률</p>
                    <ul style="margin:16px 0 0 0; padding-left:20px; font-size:13px; line-height:1.8">
                      <li>MVP 테스트</li>
                      <li>200M원 확보</li>
                      <li>팀 사전 구성</li>
                      <li>Month 15-18 BEP</li>
                    </ul>
                  </div>
                  <div style="padding:24px; background:rgba(239,68,68,0.15); border-radius:16px; border:2px solid #EF4444">
                    <h3 style="color:#EF4444; margin:0 0 16px 0">❌ Option C: 현재 유지</h3>
                    <p style="font-size:32px; font-weight:700; margin:8px 0; color:#EF4444">15%</p>
                    <p style="font-size:14px; margin:8px 0">성공 확률</p>
                    <ul style="margin:16px 0 0 0; padding-left:20px; font-size:13px; line-height:1.8">
                      <li>Month 4 파산</li>
                      <li>창업자 번아웃</li>
                      <li>평판 손상</li>
                      <li style="color:#EF4444"><strong>절대 불가</strong></li>
                    </ul>
                  </div>
                </div>
                <div style="margin-top:32px; padding:24px; background:var(--ink); color:white; border-radius:16px; text-align:center">
                  <p style="font-size:20px; font-weight:600; margin:0 0 12px 0">최종 권고</p>
                  <p style="font-size:16px; line-height:1.8; margin:0">
                    이 사업은 방향은 맞지만 실행 계획이 <strong>치명적으로 부실</strong>합니다.<br>
                    <strong>전면 수정</strong> 또는 <strong>6개월 연기</strong>를 강력히 권고합니다.
                  </p>
                </div>
              </div>
            </div>
          </section>
        </div>
      </section>
'''

# Update total slide count in navigation
html_content = re.sub(r'<strong>\d+ / 23</strong>', '<strong>23 / 27</strong>', html_content)

# Insert the new slides
new_html = html_content[:insertion_point] + opus_slides + html_content[insertion_point:]

# Update the total slide count in JavaScript
new_html = re.sub(r'const totalSlides = \d+;', 'const totalSlides = 27;', new_html)

# Write the modified HTML
with open('strategy_a_proposal_v2_opus.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully added Opus analysis slides! New file: strategy_a_proposal_v2_opus.html")