# -*- coding: utf-8 -*-
import re

# Read the HTML file
input_file = r'C:\Users\dkskr\OneDrive\111\fruits\output\strategy_a_proposal_v2.html'
output_file = r'C:\Users\dkskr\OneDrive\111\fruits\output\strategy_a_proposal_v2.html'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new slides to add
new_slides = '''      <section class="slide tone-7" data-slide-index="20" data-chapter="6">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">실행</span>
            <strong>21 / 23</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Financial Planning</div>
                  <h2 class="title">재무 계획 - 초기 자본 7,555만원과 7개월 흑자 전환 로드맵</h2>
                  <div class="desc">전략 실행을 위한 구체적 자금 계획입니다. 초기 투자 4,890만원과 6개월 누적 적자 2,665만원을 합친 7,555만원이 필요하며, 7개월차 월 500건 달성 시 흑자 전환합니다.</div>
                </div>
                <div class="pill">Capital Requirements, Cash Flow, Break-even</div>
              </div>
              <div class="board">
                <div class="chart">
                  <h3>초기 자본 투자 계획 (4,890만원)</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>항목</th>
                        <th>금액</th>
                        <th>비고</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>창업 비용</td>
                        <td>140만원</td>
                        <td>사업자 등록, 법인 설립, 인허가</td>
                      </tr>
                      <tr>
                        <td>초기 재고 매입</td>
                        <td>700만원</td>
                        <td>5 SKU, 주 1회 회전 가정</td>
                      </tr>
                      <tr>
                        <td>설비/장비</td>
                        <td>550만원</td>
                        <td>냉장고 3대, 검수장비, IT 장비</td>
                      </tr>
                      <tr>
                        <td>플랫폼 구축</td>
                        <td>150만원</td>
                        <td>스마트스토어 세팅, 사진 촬영</td>
                      </tr>
                      <tr>
                        <td>마케팅 초기 비용</td>
                        <td>1,050만원</td>
                        <td>3개월 광고비 + 브랜드 디자인</td>
                      </tr>
                      <tr>
                        <td>운영 예비비</td>
                        <td>2,300만원</td>
                        <td>인건비 3개월 + 예비 자금</td>
                      </tr>
                      <tr>
                        <td><strong>합계</strong></td>
                        <td><strong>4,890만원</strong></td>
                        <td>초기 3개월 운영 자금</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="chart">
                  <h3>월별 현금흐름 예측 (1~6개월)</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>월</th>
                        <th>예상 매출</th>
                        <th>매출원가</th>
                        <th>고정비</th>
                        <th>순손익</th>
                        <th>누적 현금</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>1개월</td>
                        <td>600만원</td>
                        <td>420만원</td>
                        <td>900만원</td>
                        <td><strong style="color:var(--accent)">-720만원</strong></td>
                        <td>-720만원</td>
                      </tr>
                      <tr>
                        <td>2개월</td>
                        <td>900만원</td>
                        <td>630만원</td>
                        <td>900만원</td>
                        <td><strong style="color:var(--accent)">-630만원</strong></td>
                        <td>-1,350만원</td>
                      </tr>
                      <tr>
                        <td>3개월</td>
                        <td>1,440만원</td>
                        <td>1,010만원</td>
                        <td>900만원</td>
                        <td><strong style="color:var(--accent)">-470만원</strong></td>
                        <td>-1,820만원</td>
                      </tr>
                      <tr>
                        <td>4개월</td>
                        <td>1,680만원</td>
                        <td>1,175만원</td>
                        <td>900만원</td>
                        <td><strong style="color:var(--accent)">-395만원</strong></td>
                        <td>-2,215만원</td>
                      </tr>
                      <tr>
                        <td>5개월</td>
                        <td>2,100만원</td>
                        <td>1,470만원</td>
                        <td>900만원</td>
                        <td><strong style="color:var(--accent)">-270만원</strong></td>
                        <td>-2,485만원</td>
                      </tr>
                      <tr>
                        <td>6개월</td>
                        <td>2,400만원</td>
                        <td>1,680만원</td>
                        <td>900만원</td>
                        <td><strong style="color:var(--accent)">-180만원</strong></td>
                        <td>-2,665만원</td>
                      </tr>
                      <tr style="background:var(--accent-bg)">
                        <td><strong>7개월</strong></td>
                        <td><strong>6,000만원</strong></td>
                        <td><strong>4,200만원</strong></td>
                        <td><strong>900만원</strong></td>
                        <td><strong style="color:var(--olive)">+900만원</strong></td>
                        <td><strong>흑자 전환</strong></td>
                      </tr>
                    </tbody>
                  </table>
                  <p style="margin-top:16px; font-size:13px; color:var(--muted)">* 고정비 = 인건비 600만원 + 마케팅비 300만원</p>
                </div>
              </div>
              <div class="board" style="margin-top:24px">
                <div class="grid-2">
                  <article class="card">
                    <h3>필요 자본 총액</h3>
                    <p><strong>초기 투자:</strong> 4,890만원</p>
                    <p><strong>6개월 적자:</strong> 2,665만원</p>
                    <p style="margin-top:8px; font-size:18px; font-weight:bold; color:var(--accent)">총 7,555만원</p>
                  </article>
                  <article class="card">
                    <h3>자금 조달 계획</h3>
                    <p><strong>자기자본:</strong> 3,000만원</p>
                    <p><strong>정부 지원금:</strong> 2,000만원</p>
                    <p><strong>차입금:</strong> 2,555만원</p>
                  </article>
                </div>
              </div>
              <div style="margin-top:32px; padding-top:16px; border-top:1px solid var(--line); font-size:11px; color:var(--muted)">
                <p style="margin:4px 0">[1] 손익분기: 7~8개월차 월 500건 달성 시 흑자 전환 예상</p>
                <p style="margin:4px 0">[2] 재무 계획 출처: business_execution_roadmap.md 재무 에이전트 분석</p>
              </div>
            </div>
          </section>
        </div>
      </section>
      <section class="slide tone-7" data-slide-index="21" data-chapter="6">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">실행</span>
            <strong>22 / 23</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Sales Channels</div>
                  <h2 class="title">판매 채널 전략 - 네이버/카카오톡/쿠팡 3대 채널 입점 로드맵</h2>
                  <div class="desc">플랫폼별 수수료, 입점 난이도, 타겟 고객을 고려한 단계별 채널 확장 전략입니다. Phase 1은 네이버 중심, Phase 2에서 카카오톡 명절 특화, Phase 3에서 쿠팡 물량 확보 순서로 진행합니다.</div>
                </div>
                <div class="pill">Platform Strategy, Fee Structure, Timeline</div>
              </div>
              <div class="board">
                <div class="chart">
                  <h3>Phase 1 우선 채널: 네이버 스마트스토어</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>항목</th>
                        <th>내용</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>수수료</strong></td>
                        <td>5.0% (가장 낮음)</td>
                      </tr>
                      <tr>
                        <td><strong>입점 난이도</strong></td>
                        <td>낮음 (1~3일 심사)</td>
                      </tr>
                      <tr>
                        <td><strong>필수 서류</strong></td>
                        <td>사업자등록증, 통신판매업 신고번호</td>
                      </tr>
                      <tr>
                        <td><strong>정산 주기</strong></td>
                        <td>주 1회 (익주 화요일)</td>
                      </tr>
                      <tr>
                        <td><strong>장점</strong></td>
                        <td>검색광고 연동, 낮은 수수료, 빠른 입점</td>
                      </tr>
                      <tr>
                        <td><strong>타겟 고객</strong></td>
                        <td>30~50대, 검색 중심 구매자</td>
                      </tr>
                      <tr>
                        <td><strong>예상 매출 비중</strong></td>
                        <td>Phase 1: 100%, Phase 2: 70%</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="chart">
                  <h3>Phase 2 확장 채널: 카카오톡 선물하기</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>항목</th>
                        <th>내용</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>수수료</strong></td>
                        <td>19~25% (매우 높음)</td>
                      </tr>
                      <tr>
                        <td><strong>입점 난이도</strong></td>
                        <td>높음 (4~6주, 샘플 심사)</td>
                      </tr>
                      <tr>
                        <td><strong>필수 요구사항</strong></td>
                        <td>프리미엄 포장, 전국 배송, 생산물 배상책임보험</td>
                      </tr>
                      <tr>
                        <td><strong>정산 주기</strong></td>
                        <td>월 2회 (15일, 말일)</td>
                      </tr>
                      <tr>
                        <td><strong>장점</strong></td>
                        <td>명절 특수 (설/추석 매출 30~40%)</td>
                      </tr>
                      <tr>
                        <td><strong>입점 시기</strong></td>
                        <td>D+60일 (설 명절 2개월 전)</td>
                      </tr>
                      <tr>
                        <td><strong>전략적 역할</strong></td>
                        <td>선물형 세그먼트 집중, 브랜드 신뢰도 향상</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
              <div class="board" style="margin-top:24px">
                <div class="chart">
                  <h3>Phase 3 물량 채널: 쿠팡 Wing/로켓배송</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>구분</th>
                        <th>쿠팡 Wing (초기)</th>
                        <th>로켓배송 (확장)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>수수료</strong></td>
                        <td>10~13%</td>
                        <td>15~20% (협상)</td>
                      </tr>
                      <tr>
                        <td><strong>입점 난이도</strong></td>
                        <td>낮음 (1~2주)</td>
                        <td>매우 높음 (월 1,000건+ 물량)</td>
                      </tr>
                      <tr>
                        <td><strong>배송</strong></td>
                        <td>자체 배송 (CJ/롯데)</td>
                        <td>쿠팡 물류센터</td>
                      </tr>
                      <tr>
                        <td><strong>권장 시점</strong></td>
                        <td>Phase 2 (테스트용)</td>
                        <td>Phase 3 (월 500건 달성 후)</td>
                      </tr>
                      <tr>
                        <td><strong>장점</strong></td>
                        <td>빠른 입점, 트래픽 높음</td>
                        <td>로켓배송 브랜드 파워</td>
                      </tr>
                      <tr>
                        <td><strong>단점</strong></td>
                        <td>가격 경쟁 치열</td>
                        <td>물량 요구, 마진 압박</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
              <div class="board" style="margin-top:24px">
                <div class="grid-2">
                  <article class="card">
                    <h3>채널 확장 타임라인</h3>
                    <p><strong>D-Day:</strong> 네이버 스마트스토어</p>
                    <p><strong>D+60:</strong> 카카오톡 선물하기 신청</p>
                    <p><strong>D+120:</strong> 쿠팡 Wing 테스트</p>
                    <p><strong>D+180:</strong> 로켓배송 협상 시작</p>
                  </article>
                  <article class="card">
                    <h3>핵심 전략</h3>
                    <p><strong>수수료 최적화:</strong> 네이버 5% 중심</p>
                    <p><strong>명절 특수:</strong> 카카오톡 집중</p>
                    <p><strong>물량 확보:</strong> 쿠팡은 500건 이후</p>
                  </article>
                </div>
              </div>
              <div style="margin-top:32px; padding-top:16px; border-top:1px solid var(--line); font-size:11px; color:var(--muted)">
                <p style="margin:4px 0">[1] 플랫폼별 상세 요구사항: business_execution_roadmap.md 참조</p>
                <p style="margin:4px 0">[2] 11번가, G마켓, 옥션은 트래픽 감소로 초기 비권장</p>
              </div>
            </div>
          </section>
        </div>
      </section>
      <section class="slide tone-7" data-slide-index="22" data-chapter="6">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">실행</span>
            <strong>23 / 23</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Influencer Marketing</div>
                  <h2 class="title">소규모 인플루언서 공동구매 - 일반 광고 대비 625% 순이익 증대</h2>
                  <div class="desc">나노/마이크로 인플루언서(팔로워 3천~5만)와 공동구매 협업으로 CAC 72% 절감과 ROI 4배 이상을 달성합니다. 월 10명 협업 시 620건 판매, 1,782만원 순이익으로 일반 광고 대비 390만원 더 효율적입니다.</div>
                </div>
                <div class="pill">Nano/Micro Influencers, Co-buying Events, ROI 4x</div>
              </div>
              <div class="board">
                <div class="chart">
                  <h3>마진 계산 방식 (15% 할인 공동구매)</h3>
                  <p>샘플: 샤인머스캣 2kg 선물세트 (정상가 89,000원)</p>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>항목</th>
                        <th>일반 판매</th>
                        <th>공동구매</th>
                        <th>차이</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>판매가</td>
                        <td>89,000원</td>
                        <td>75,650원</td>
                        <td>-13,350원</td>
                      </tr>
                      <tr>
                        <td>매출원가</td>
                        <td>45,300원</td>
                        <td>45,300원</td>
                        <td>-</td>
                      </tr>
                      <tr>
                        <td>플랫폼 수수료 (5%)</td>
                        <td>4,450원</td>
                        <td>3,783원</td>
                        <td>-667원</td>
                      </tr>
                      <tr>
                        <td>배송비</td>
                        <td>4,500원</td>
                        <td>4,500원</td>
                        <td>-</td>
                      </tr>
                      <tr>
                        <td>마케팅비/커미션</td>
                        <td>14,200원 (CAC)</td>
                        <td>7,565원 (10%)</td>
                        <td>-6,635원</td>
                      </tr>
                      <tr>
                        <td><strong>공헌이익</strong></td>
                        <td><strong>20,550원</strong></td>
                        <td><strong>14,502원</strong></td>
                        <td>-6,048원</td>
                      </tr>
                      <tr style="background:var(--olive-bg)">
                        <td><strong>마케팅비 절감</strong></td>
                        <td>-</td>
                        <td><strong>+14,200원</strong></td>
                        <td>-</td>
                      </tr>
                      <tr style="background:var(--accent-bg)">
                        <td><strong>실질 이익</strong></td>
                        <td><strong>20,550원</strong></td>
                        <td><strong>28,702원</strong></td>
                        <td><strong style="color:var(--olive)">+8,152원</strong></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="chart">
                  <h3>인플루언서 커미션 구조 (권장)</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>타입</th>
                        <th>팔로워</th>
                        <th>커미션</th>
                        <th>예상 판매</th>
                        <th>ROI</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>나노</strong></td>
                        <td>3천~1만</td>
                        <td>8%</td>
                        <td>30~50건</td>
                        <td><strong>4.7배</strong></td>
                      </tr>
                      <tr>
                        <td><strong>마이크로</strong></td>
                        <td>1만~5만</td>
                        <td>10%</td>
                        <td>100~150건</td>
                        <td><strong>4.2배</strong></td>
                      </tr>
                      <tr>
                        <td>미드 (Phase 3)</td>
                        <td>5만~10만</td>
                        <td>12%</td>
                        <td>200건+</td>
                        <td>2.5배</td>
                      </tr>
                    </tbody>
                  </table>
                  <p style="margin-top:16px; font-size:13px"><strong>핵심:</strong> 나노/마이크로 인플루언서가 ROI 가장 높음 (참여율 5~8%)</p>
                </div>
              </div>
              <div class="board" style="margin-top:24px">
                <div class="chart">
                  <h3>월간 공동구매 운영 계획 (Phase 2: D+60~)</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>주차</th>
                        <th>인플루언서 수</th>
                        <th>타겟 판매</th>
                        <th>총 커미션</th>
                        <th>순이익</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>1주차</td>
                        <td>나노 3명</td>
                        <td>120건</td>
                        <td>72만원</td>
                        <td>345만원</td>
                      </tr>
                      <tr>
                        <td>2주차</td>
                        <td>마이크로 2명</td>
                        <td>200건</td>
                        <td>165만원</td>
                        <td>575만원</td>
                      </tr>
                      <tr>
                        <td>3주차</td>
                        <td>나노 3명</td>
                        <td>120건</td>
                        <td>72만원</td>
                        <td>345만원</td>
                      </tr>
                      <tr>
                        <td>4주차</td>
                        <td>마이크로 1 + 나노 2</td>
                        <td>180건</td>
                        <td>123만원</td>
                        <td>517만원</td>
                      </tr>
                      <tr style="background:var(--accent-bg)">
                        <td><strong>월 합계</strong></td>
                        <td><strong>11명</strong></td>
                        <td><strong>620건</strong></td>
                        <td><strong>432만원</strong></td>
                        <td><strong>1,782만원</strong></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="chart">
                  <h3>vs. 일반 광고 성과 비교 (월 기준)</h3>
                  <table class="table" style="margin-top:16px">
                    <thead>
                      <tr>
                        <th>지표</th>
                        <th>일반 광고</th>
                        <th>공동구매</th>
                        <th>개선율</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>월 판매</strong></td>
                        <td>120건</td>
                        <td>620건</td>
                        <td style="color:var(--olive)">+417%</td>
                      </tr>
                      <tr>
                        <td><strong>CAC</strong></td>
                        <td>25,000원</td>
                        <td>6,968원</td>
                        <td style="color:var(--olive)">-72%</td>
                      </tr>
                      <tr>
                        <td><strong>순이익</strong></td>
                        <td>246만원</td>
                        <td>1,782만원</td>
                        <td style="color:var(--olive)">+625%</td>
                      </tr>
                      <tr>
                        <td><strong>ROI</strong></td>
                        <td>0.82배</td>
                        <td>4.12배</td>
                        <td style="color:var(--olive)">+402%</td>
                      </tr>
                      <tr style="background:var(--olive-bg)">
                        <td><strong>월 추가 이익</strong></td>
                        <td colspan="3"><strong>+1,536만원 (공동구매가 더 효율적)</strong></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
              <div class="board" style="margin-top:24px">
                <div class="grid-3">
                  <article class="card">
                    <h3>인플루언서 선정 기준</h3>
                    <p><strong>참여율:</strong> 5% 이상 (핵심)</p>
                    <p><strong>니치:</strong> 육아, 요리, 건강, 선물</p>
                    <p><strong>협찬 비율:</strong> 30% 이하</p>
                  </article>
                  <article class="card">
                    <h3>발굴 채널</h3>
                    <p><strong>인스타그램:</strong> 해시태그 검색</p>
                    <p><strong>플랫폼:</strong> 레뷰(revu.net)</p>
                    <p><strong>블로그:</strong> 네이버 상위 블로거</p>
                  </article>
                  <article class="card">
                    <h3>실행 타임라인</h3>
                    <p><strong>Phase 1:</strong> 나노 3명 테스트</p>
                    <p><strong>Phase 2:</strong> 월 10명 본격 확대</p>
                    <p><strong>Phase 3:</strong> 앰배서더 운영</p>
                  </article>
                </div>
              </div>
              <div style="margin-top:32px; padding-top:16px; border-top:1px solid var(--line); font-size:11px; color:var(--muted)">
                <p style="margin:4px 0">[1] 상세 전략 및 DM 템플릿: influencer_coop_buying_strategy.md 참조</p>
                <p style="margin:4px 0">[2] 성과 시뮬레이션: 나노(팔로워 5천) 40건 판매 시 순이익 115만원, ROI 4.74배 검증됨</p>
              </div>
            </div>
          </section>
        </div>
      </section>
'''

# Find the insertion point (before closing </div></main>)
insertion_point = content.find('    </div>\n  </main>')

if insertion_point == -1:
    print("Error: Could not find insertion point")
else:
    # Insert new slides
    content = content[:insertion_point] + new_slides + content[insertion_point:]

    # Write back to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully added 3 new slides (index 20, 21, 22)")
    print("- Slide 20: Financial Planning")
    print("- Slide 21: Sales Channels Strategy")
    print("- Slide 22: Influencer Co-buying Strategy")
    print(f"Total slides now: 23 (index 0-22)")
