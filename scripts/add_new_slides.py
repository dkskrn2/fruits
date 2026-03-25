import re

# Read current HTML
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Creating 5 new slides from markdown files...")

# Slide 18: SKU Profitability Analysis
slide_18 = '''      <section class="slide tone-7" data-slide-index="18" data-chapter="6">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">수익성</span>
            <strong>19 / 23</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">SKU Profitability</div>
                  <h2 class="title">SKU별 수익성 분석 - 선물형과 일상형의 공헌이익 구조</h2>
                  <div class="desc">추상적 전략을 구체적 수익 모델로 검증합니다. 선물형 SKU는 28%+ 마진율로 고객단가 전략을 뒷받침하고, 일상형은 합배송 구조에서 재구매 유도 역할을 맡습니다.</div>
                </div>
                <div class="pill">28.7% Margin on Gift SKUs</div>
              </div>
              <div class="board">
                <div class="chart">
                  <h3>선물형 SKU 수익성 (고마진)</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>항목</th>
                        <th>샤인머스캣 2kg</th>
                        <th>사과·배 혼합 3kg</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>판매가</td>
                        <td><strong>89,000원</strong></td>
                        <td><strong>75,000원</strong></td>
                      </tr>
                      <tr>
                        <td>원가 (산지 직거래)</td>
                        <td>45,000원</td>
                        <td>38,000원</td>
                      </tr>
                      <tr>
                        <td>포장재 (고급)</td>
                        <td>7,000원</td>
                        <td>5,500원</td>
                      </tr>
                      <tr>
                        <td>배송비</td>
                        <td>4,500원</td>
                        <td>4,500원</td>
                      </tr>
                      <tr>
                        <td>보상비용 (10% 이슈율)</td>
                        <td>2,500원</td>
                        <td>2,000원</td>
                      </tr>
                      <tr>
                        <td>플랫폼 수수료 (5%)</td>
                        <td>4,450원</td>
                        <td>3,750원</td>
                      </tr>
                      <tr style="background: rgba(203, 91, 44, 0.1)">
                        <td><strong>공헌이익</strong></td>
                        <td><strong>25,550원 (28.7%)</strong></td>
                        <td><strong>21,250원 (28.3%)</strong></td>
                      </tr>
                      <tr>
                        <td>손익분기 주문량</td>
                        <td>120건/월</td>
                        <td>140건/월</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="chart">
                  <h3>일상형 SKU 수익성 (재구매 유도)</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>항목</th>
                        <th>가족 사과 5kg</th>
                        <th>방울토마토 1kg</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>판매가</td>
                        <td><strong>35,000원</strong></td>
                        <td><strong>18,000원</strong></td>
                      </tr>
                      <tr>
                        <td>원가</td>
                        <td>18,000원</td>
                        <td>9,000원</td>
                      </tr>
                      <tr>
                        <td>포장재 (표준)</td>
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
                        <td>플랫폼 수수료 (5%)</td>
                        <td>1,750원</td>
                        <td>900원</td>
                      </tr>
                      <tr style="background: rgba(85, 101, 72, 0.1)">
                        <td><strong>공헌이익</strong></td>
                        <td><strong>8,050원 (23.0%)</strong></td>
                        <td><strong>3,200원 (17.8%)</strong></td>
                      </tr>
                      <tr>
                        <td>전략적 역할</td>
                        <td>재구매 유도 + 리뷰</td>
                        <td>합배송 유도 상품</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
              <div style="margin-top:24px; padding:16px; background:rgba(203,91,44,0.08); border-radius:12px">
                <p style="font-size:13px; line-height:1.6; margin:0"><strong>핵심 시사점:</strong> 선물형 28%+ 고마진으로 초기 고정비 회수 가능. 일상형은 단독 판매 시 적자이나 합배송/정기구독 모델로 재구매율 확보하는 전략적 SKU로 설계됨.</p>
              </div>
            </div>
          </section>
        </div>
      </section>'''

# Slide 19: Financial Planning
slide_19 = '''      <section class="slide tone-7" data-slide-index="19" data-chapter="6">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">재무</span>
            <strong>20 / 23</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Financial Planning</div>
                  <h2 class="title">재무 계획 - 초기 자본 7,555만원과 7개월 흑자 전환 로드맵</h2>
                  <div class="desc">전략 실행을 위한 구체적 자금 계획입니다. 초기 투자 4,890만원과 6개월 누적 적자 2,665만원을 합친 7,555만원이 필요하며, 7개월차 월 500건 달성 시 흑자 전환합니다.</div>
                </div>
                <div class="pill">7개월 Break-even, 500건/월</div>
              </div>
              <div class="board">
                <div class="chart">
                  <h3>초기 자본 투자 계획 (4,890만원)</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>구분</th>
                        <th>항목</th>
                        <th>금액</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td rowspan="3">창업비용</td>
                        <td>사업자 등록 + 통신판매업</td>
                        <td>10만원</td>
                      </tr>
                      <tr>
                        <td>법인 설립 (선택)</td>
                        <td>100만원</td>
                      </tr>
                      <tr>
                        <td>인허가 비용</td>
                        <td>30만원</td>
                      </tr>
                      <tr>
                        <td rowspan="2">초기 재고</td>
                        <td>1차 재고 (5 SKU)</td>
                        <td>500만원</td>
                      </tr>
                      <tr>
                        <td>포장재 초도 물량</td>
                        <td>200만원</td>
                      </tr>
                      <tr>
                        <td rowspan="3">설비/장비</td>
                        <td>냉장 보관 시설</td>
                        <td>300만원</td>
                      </tr>
                      <tr>
                        <td>검수/포장 장비</td>
                        <td>100만원</td>
                      </tr>
                      <tr>
                        <td>IT 장비</td>
                        <td>150만원</td>
                      </tr>
                      <tr>
                        <td rowspan="2">플랫폼</td>
                        <td>스마트스토어 세팅</td>
                        <td>50만원</td>
                      </tr>
                      <tr>
                        <td>제품 사진 촬영</td>
                        <td>100만원</td>
                      </tr>
                      <tr>
                        <td rowspan="2">마케팅</td>
                        <td>1차 마케팅 (3개월)</td>
                        <td>900만원</td>
                      </tr>
                      <tr>
                        <td>브랜드 디자인</td>
                        <td>150만원</td>
                      </tr>
                      <tr>
                        <td rowspan="2">운영비</td>
                        <td>3개월 인건비</td>
                        <td>1,800만원</td>
                      </tr>
                      <tr>
                        <td>예비 자금</td>
                        <td>500만원</td>
                      </tr>
                      <tr style="background: rgba(203, 91, 44, 0.15)">
                        <td colspan="2"><strong>합계</strong></td>
                        <td><strong>4,890만원</strong></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="chart">
                  <h3>월별 현금흐름 예측 (6개월)</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>월</th>
                        <th>매출</th>
                        <th>고정비</th>
                        <th>순손익</th>
                        <th>누적</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>1개월</td>
                        <td>600만원 (50건)</td>
                        <td>900만원</td>
                        <td style="color:#a14253">-720만원</td>
                        <td>-720만원</td>
                      </tr>
                      <tr>
                        <td>2개월</td>
                        <td>900만원 (75건)</td>
                        <td>900만원</td>
                        <td style="color:#a14253">-630만원</td>
                        <td>-1,350만원</td>
                      </tr>
                      <tr>
                        <td>3개월</td>
                        <td>1,440만원 (120건)</td>
                        <td>900만원</td>
                        <td style="color:#a14253">-470만원</td>
                        <td>-1,820만원</td>
                      </tr>
                      <tr>
                        <td>4개월</td>
                        <td>1,680만원 (140건)</td>
                        <td>900만원</td>
                        <td style="color:#a14253">-395만원</td>
                        <td>-2,215만원</td>
                      </tr>
                      <tr>
                        <td>5개월</td>
                        <td>2,100만원 (175건)</td>
                        <td>900만원</td>
                        <td style="color:#a14253">-270만원</td>
                        <td>-2,485만원</td>
                      </tr>
                      <tr>
                        <td>6개월</td>
                        <td>2,400만원 (200건)</td>
                        <td>900만원</td>
                        <td style="color:#a14253">-180만원</td>
                        <td>-2,665만원</td>
                      </tr>
                      <tr style="background: rgba(85, 101, 72, 0.1)">
                        <td><strong>7~8개월</strong></td>
                        <td><strong>6,000만원 (500건)</strong></td>
                        <td><strong>900만원</strong></td>
                        <td style="color:#556548"><strong>흑자 전환</strong></td>
                        <td>-</td>
                      </tr>
                    </tbody>
                  </table>
                  <div style="margin-top:20px; padding:14px; background:rgba(85,101,72,0.08); border-radius:10px">
                    <p style="font-size:12px; line-height:1.5; margin:0"><strong>필요 자본 총액:</strong> 초기 투자 4,890만원 + 6개월 누적 적자 2,665만원 = <strong>7,555만원</strong><br>
                    <strong>손익분기:</strong> 월 고정비 900만원 ÷ 평균 공헌이익 18,000원 = <strong>500건/월</strong> (7~8개월차 달성 목표)</p>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </section>'''

# Slide 20: Sales Channels
slide_20 = '''      <section class="slide tone-7" data-slide-index="20" data-chapter="6">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">채널</span>
            <strong>21 / 23</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Sales Channels</div>
                  <h2 class="title">판매 채널 전략 - 네이버/카카오톡/쿠팡 3대 채널 입점 로드맵</h2>
                  <div class="desc">플랫폼별 수수료, 입점 난이도, 타겟 고객을 고려한 단계별 채널 확장 전략입니다. Phase 1은 네이버 중심, Phase 2에서 카카오톡 명절 특화, Phase 3에서 쿠팡 물량 확보 순서로 진행합니다.</div>
                </div>
                <div class="pill">Phase 1: Naver → Phase 2: Kakao → Phase 3: Coupang</div>
              </div>
              <div class="board">
                <div class="chart">
                  <h3>플랫폼별 비교 분석</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>구분</th>
                        <th>네이버 스마트스토어</th>
                        <th>카카오톡 선물하기</th>
                        <th>쿠팡 Wing</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>수수료</td>
                        <td><strong>5.0%</strong></td>
                        <td>19.0~25.0%</td>
                        <td>10.0~13.0%</td>
                      </tr>
                      <tr>
                        <td>정산 주기</td>
                        <td>주 1회 (익주 화요일)</td>
                        <td>월 2회 (15일, 말일)</td>
                        <td>월 2회</td>
                      </tr>
                      <tr>
                        <td>심사 기간</td>
                        <td>1~3일</td>
                        <td>2~4주 (샘플 심사)</td>
                        <td>1~2주</td>
                      </tr>
                      <tr>
                        <td>필수 조건</td>
                        <td>통신판매업 신고</td>
                        <td>생산물 배상책임보험</td>
                        <td>최소 월 1,000건</td>
                      </tr>
                      <tr>
                        <td>강점</td>
                        <td>낮은 수수료, 빠른 입점</td>
                        <td>선물 수요 집중 (명절)</td>
                        <td>압도적 트래픽</td>
                      </tr>
                      <tr>
                        <td>약점</td>
                        <td>경쟁 과다</td>
                        <td>고수수료, 까다로운 심사</td>
                        <td>물량 요구 높음</td>
                      </tr>
                      <tr>
                        <td>타겟 고객</td>
                        <td>가족 루틴형, 일상형</td>
                        <td>선물형, 돌봄형</td>
                        <td>가격 민감 고객</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="chart">
                  <h3>단계별 입점 로드맵</h3>
                  <div style="margin-top:16px">
                    <div style="margin-bottom:20px; padding:16px; background:rgba(203,91,44,0.08); border-radius:12px">
                      <h4 style="margin:0 0 10px 0; font-size:14px; color:#cb5b2c">Phase 1 (D+0~90일): 네이버 집중</h4>
                      <p style="font-size:13px; line-height:1.6; margin:0"><strong>목표:</strong> 월 120~200건 달성, 리뷰 30개 이상 확보<br>
                      <strong>전략:</strong> 검색광고 월 300만원, 상세페이지 A/B 테스트, 초기 후기 이벤트<br>
                      <strong>핵심 KPI:</strong> 전환율 1.5%+, 재구매율 20%+</p>
                    </div>
                    <div style="margin-bottom:20px; padding:16px; background:rgba(85,101,72,0.08); border-radius:12px">
                      <h4 style="margin:0 0 10px 0; font-size:14px; color:#556548">Phase 2 (D+90~180일): 카카오톡 추가</h4>
                      <p style="font-size:13px; line-height:1.6; margin:0"><strong>목표:</strong> 명절 (설/추석) 선물 수요 집중 공략<br>
                      <strong>전략:</strong> 샘플 심사 통과, 선물형 SKU 포장 고급화, 기업 선물 문의 대응<br>
                      <strong>핵심 KPI:</strong> 명절 2주간 200건 이상, 평균 객단가 85,000원+</p>
                    </div>
                    <div style="margin-bottom:0; padding:16px; background:rgba(161,66,83,0.08); border-radius:12px">
                      <h4 style="margin:0 0 10px 0; font-size:14px; color:#a14253">Phase 3 (D+180일~): 쿠팡 확장</h4>
                      <p style="font-size:13px; line-height:1.6; margin:0"><strong>전제 조건:</strong> 월 300건 이상 안정화, 운영 인력 2명 이상<br>
                      <strong>전략:</strong> 물량 확보 협상, 로켓배송 자격 심사, 가격 경쟁력 확보<br>
                      <strong>주의사항:</strong> 높은 수수료와 물량 요구, 초기 단계에서는 비권장</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </section>'''

# Slide 21: Influencer Co-buying
slide_21 = '''      <section class="slide tone-7" data-slide-index="21" data-chapter="6">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">마케팅</span>
            <strong>22 / 23</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Influencer Marketing</div>
                  <h2 class="title">소규모 인플루언서 공동구매 - 일반 광고 대비 625% 순이익 증대</h2>
                  <div class="desc">나노/마이크로 인플루언서(팔로워 3천~5만)와 공동구매 협업으로 CAC 72% 절감과 ROI 4배 이상을 달성합니다. 월 10명 협업 시 620건 판매, 1,782만원 순이익으로 일반 광고 대비 390만원 더 효율적입니다.</div>
                </div>
                <div class="pill">ROI 4.1x, CAC 72% Reduction</div>
              </div>
              <div class="board">
                <div class="chart">
                  <h3>일반 광고 vs 공동구매 성과 비교</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>항목</th>
                        <th>일반 광고 (네이버)</th>
                        <th>공동구매</th>
                        <th>개선폭</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>월 마케팅비</td>
                        <td>300만원 (고정)</td>
                        <td>432만원 (커미션)</td>
                        <td>+44%</td>
                      </tr>
                      <tr>
                        <td>월 판매 건수</td>
                        <td>120건</td>
                        <td><strong>620건</strong></td>
                        <td style="color:#556548"><strong>+417%</strong></td>
                      </tr>
                      <tr>
                        <td>CAC (고객획득비용)</td>
                        <td>25,000원</td>
                        <td><strong>6,968원</strong></td>
                        <td style="color:#556548"><strong>-72%</strong></td>
                      </tr>
                      <tr>
                        <td>전환율</td>
                        <td>1.5%</td>
                        <td>5~8%</td>
                        <td>+3.3~5.3배</td>
                      </tr>
                      <tr>
                        <td>월 순이익</td>
                        <td>246만원</td>
                        <td><strong>1,782만원</strong></td>
                        <td style="color:#556548"><strong>+625%</strong></td>
                      </tr>
                      <tr style="background: rgba(85, 101, 72, 0.15)">
                        <td><strong>ROI</strong></td>
                        <td>0.82배</td>
                        <td><strong>4.1배</strong></td>
                        <td style="color:#556548"><strong>+5배</strong></td>
                      </tr>
                    </tbody>
                  </table>
                  <div style="margin-top:16px; padding:12px; background:rgba(203,91,44,0.08); border-radius:10px">
                    <p style="font-size:12px; line-height:1.5; margin:0"><strong>핵심 원리:</strong> CAC를 0원으로 만들어 실질 수익성 향상. 15% 할인하지만 마케팅비 14,200원 절감으로 건당 +8,152원 이익 증가.</p>
                  </div>
                </div>
                <div class="chart">
                  <h3>타겟 인플루언서 프로필 & 커미션 구조</h3>
                  <div style="margin-top:16px">
                    <table class="table">
                      <thead>
                        <tr>
                          <th>구분</th>
                          <th>나노</th>
                          <th>마이크로</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>팔로워 수</td>
                          <td>3,000~10,000명</td>
                          <td>10,000~50,000명</td>
                        </tr>
                        <tr>
                          <td>참여율 (ER)</td>
                          <td>5~8%</td>
                          <td>3~5%</td>
                        </tr>
                        <tr>
                          <td>커미션율</td>
                          <td><strong>8%</strong></td>
                          <td><strong>10%</strong></td>
                        </tr>
                        <tr>
                          <td>예상 판매</td>
                          <td>30~50건/회</td>
                          <td>100~150건/회</td>
                        </tr>
                        <tr>
                          <td>전환율</td>
                          <td>20~30%</td>
                          <td>15~25%</td>
                        </tr>
                        <tr>
                          <td>ROI</td>
                          <td>4~5배</td>
                          <td>3.5~4.5배</td>
                        </tr>
                        <tr>
                          <td>니치</td>
                          <td colspan="2">육아, 요리, 건강, 일상 브이로그</td>
                        </tr>
                      </tbody>
                    </table>
                    <div style="margin-top:20px; padding:14px; background:rgba(85,101,72,0.08); border-radius:10px">
                      <h4 style="margin:0 0 10px 0; font-size:13px">월 실행 계획 (Phase 1)</h4>
                      <p style="font-size:12px; line-height:1.6; margin:0"><strong>목표:</strong> 나노 8명 + 마이크로 2명 = 월 10명 협업<br>
                      <strong>예상 성과:</strong> 620건 판매 (나노 320건 + 마이크로 300건)<br>
                      <strong>총 커미션:</strong> 432만원 (공동구매가 기준 10%)<br>
                      <strong>순이익:</strong> 1,782만원 (일반 광고 246만원 대비 +1,536만원)</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </section>'''

# Slide 22: Multi-Agent Analysis
slide_22 = '''      <section class="slide tone-1" data-slide-index="22" data-chapter="0">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">검증</span>
            <strong>23 / 23</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Multi-Agent Validation</div>
                  <h2 class="title">6개 전문 에이전트 종합 분석 - 전략 완성도 9.2/10 검증</h2>
                  <div class="desc">Strategy A를 전략, 데이터, 경쟁력, 실행, UX, 리스크 6개 관점에서 독립 검증했습니다. 전략적 일관성 만점(10/10), 실행 구체성 우수(9/10)하며, 데이터 출처 보강과 UX 예시 추가로 사업계획서 수준 완성 가능합니다.</div>
                </div>
                <div class="pill">Overall Score: 9.2 / 10.0</div>
              </div>
              <div class="board">
                <div class="chart">
                  <h3>6개 에이전트 평가 점수</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>에이전트</th>
                        <th>점수</th>
                        <th>핵심 평가</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>전략 일관성</strong></td>
                        <td style="color:#556548"><strong>10.0 / 10.0</strong></td>
                        <td>"섭취 환경 설계" 메시지가 전 슬라이드 관통</td>
                      </tr>
                      <tr>
                        <td><strong>데이터 검증</strong></td>
                        <td>8.5 / 10.0</td>
                        <td>TAM/SAM 추가, 일부 출처 보강 필요</td>
                      </tr>
                      <tr>
                        <td><strong>경쟁력 분석</strong></td>
                        <td style="color:#556548"><strong>9.5 / 10.0</strong></td>
                        <td>온브릭스 3대 약점 구체화, 경쟁사 포지셔닝 명확</td>
                      </tr>
                      <tr>
                        <td><strong>실행 가능성</strong></td>
                        <td>9.0 / 10.0</td>
                        <td>SKU 수익성 검증, 손익 가드레일 명확</td>
                      </tr>
                      <tr>
                        <td><strong>UX 분석</strong></td>
                        <td>9.0 / 10.0</td>
                        <td>세그먼트 오퍼 구체적, 결정 대행 예시 추가 권장</td>
                      </tr>
                      <tr>
                        <td><strong>리스크 분석</strong></td>
                        <td>8.0 / 10.0</td>
                        <td>사업 리스크 8개 명시, 대응 전략 구체화</td>
                      </tr>
                      <tr style="background: rgba(85, 101, 72, 0.15)">
                        <td colspan="2"><strong>종합 평가 (가중평균)</strong></td>
                        <td><strong>9.2 / 10.0 ⭐⭐⭐⭐⭐</strong></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="chart">
                  <h3>V1 → V2 주요 개선사항</h3>
                  <div style="margin-top:16px">
                    <div style="margin-bottom:14px; padding:14px; background:rgba(85,101,72,0.08); border-radius:10px">
                      <h4 style="margin:0 0 8px 0; font-size:13px; color:#556548">✅ 정량 지표 대폭 보강 (+0.7점)</h4>
                      <ul style="margin:0; padding-left:20px; font-size:12px; line-height:1.6">
                        <li>TAM 3조 6천억원, SAM 7,200억원 추가</li>
                        <li>SKU별 공헌이익 분석 슬라이드 추가 (28.7%, 23.0%)</li>
                        <li>경쟁사 매출 비교 (컬리 2.2조, 오아시스 5,171억)</li>
                      </ul>
                    </div>
                    <div style="margin-bottom:14px; padding:14px; background:rgba(203,91,44,0.08); border-radius:10px">
                      <h4 style="margin:0 0 8px 0; font-size:13px; color:#cb5b2c">✅ 경쟁 전략 구체화 (+0.5점)</h4>
                      <ul style="margin:0; padding-left:20px; font-size:12px; line-height:1.6">
                        <li>온브릭스 3대 약점 정면 공략 (정보 투명성, 보장제, 타겟 분화)</li>
                        <li>경쟁 포지셔닝 맵 추가 (과일 전문성 × 듀얼 모델)</li>
                        <li>"브랜드 인지도 제로" 약점 솔직히 인정 → 신뢰도 ↑</li>
                      </ul>
                    </div>
                    <div style="margin-bottom:14px; padding:14px; background:rgba(161,66,83,0.08); border-radius:10px">
                      <h4 style="margin:0 0 8px 0; font-size:13px; color:#a14253">✅ 실행 계획 정밀화 (+0.4점)</h4>
                      <ul style="margin:0; padding-left:20px; font-size:12px; line-height:1.6">
                        <li>Phase 1/2 실험 가설-비교안-성공 기준 삼박자</li>
                        <li>손익분기 120~280건/월 SKU별 분리</li>
                        <li>세그먼트별 KPI 추적 지표 명확화</li>
                      </ul>
                    </div>
                    <div style="padding:14px; background:rgba(169,139,87,0.08); border-radius:10px">
                      <h4 style="margin:0 0 8px 0; font-size:13px; color:#a97828">🟠 남은 개선 과제 (9.2 → 9.5+ 목표)</h4>
                      <ul style="margin:0; padding-left:20px; font-size:12px; line-height:1.6">
                        <li>결정 대행 UX 구체적 예시 (화면 mockup 또는 시나리오)</li>
                        <li>일부 데이터 출처 보강 (92, 88, 84 등 수치 근거)</li>
                        <li>운영 디테일 추가 (인력 구성, 일일 처리 용량)</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </section>'''

# Find where to insert (after slide 17)
lines = content.splitlines(keepends=True)

# Find the end of slide 17
slide_17_end = None
for i, line in enumerate(lines):
    if 'data-slide-index="17"' in line:
        # Find the closing </section> for this slide
        for j in range(i+1, len(lines)):
            if '</section>' in lines[j]:
                # Check if next line starts a new slide or is end of main section
                if j+1 < len(lines) and ('</div>' in lines[j+1] or '</main>' in lines[j+1]):
                    slide_17_end = j + 1
                    break
        break

if slide_17_end is None:
    print("ERROR: Could not find slide 17 end")
    exit(1)

print(f"Found slide 17 end at line {slide_17_end}")

# Insert all 5 new slides
new_slides = '\n' + slide_18 + '\n' + slide_19 + '\n' + slide_20 + '\n' + slide_21 + '\n' + slide_22 + '\n'
new_lines = lines[:slide_17_end] + [new_slides] + lines[slide_17_end:]
new_content = ''.join(new_lines)

# Update slide counters in existing slides (X / 29 -> X / 23)
new_content = re.sub(r'(\d+) / 29', lambda m: f"{m.group(1)} / 23", new_content)
new_content = re.sub(r'(\d+) / 20', lambda m: f"{m.group(1)} / 23", new_content)

# Write updated HTML
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SUCCESS: Added 5 new slides")
print("- Slide 18: SKU Profitability Analysis")
print("- Slide 19: Financial Planning (7,555M won)")
print("- Slide 20: Sales Channels Strategy")
print("- Slide 21: Influencer Co-buying")
print("- Slide 22: 6-Agent Validation")
print("\nTotal slides: 23 (index 0-22)")
print("Updated all slide counters to '/ 23'")
