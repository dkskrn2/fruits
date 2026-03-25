#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# v2 파일 읽기
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Starting slide enhancements...")

# ========================================
# 슬라이드 #3 보강: TAM/SAM 정량화
# ========================================
old_slide_3_desc = r'<div class="desc">과일은 좋은 식품이지만, 결제는 품질만으로 일어나지 않습니다\. 실제 결제는 지금 바로 먹기 쉬운가, 버리지 않는가, 실패하지 않는가,\s+누군가를 챙기는 명분이 있는가에서 완성됩니다\.</div>'

new_slide_3_desc = '''<div class="desc">과일은 좋은 식품이지만, 결제는 품질만으로 일어나지 않습니다. 실제 결제는 지금 바로 먹기 쉬운가, 버리지 않는가, 실패하지 않는가,
                    누군가를 챙기는 명분이 있는가에서 완성됩니다. <strong>우리의 TAM은 30~49세 기혼 여성 248만 명 × 월 12만원 = 약 3조 6천억 원, 프리미엄 과일 선호층 SAM은 7,200억 원입니다.</strong></div>'''

content = re.sub(old_slide_3_desc, new_slide_3_desc, content)
print("✓ Slide #3 enhanced (TAM/SAM added)")

# ========================================
# 슬라이드 #10 (원래 #10, 지금은 #11) 보강: 온브릭스 약점 구체화
# ========================================
# "기존 강자들이..." 제목을 더 구체적으로
old_title_10 = r'<h2 class="title">기존 강자들이 선물과 프리미엄 언어가 강하다면, 우리는 일상 소비 복원 언어로 달라야 합니다</h2>'
new_title_10 = '''<h2 class="title">온브릭스(1,030억 누적 매출) 3대 약점을 정면 공략합니다</h2>'''

content = re.sub(old_title_10, new_title_10, content)

# desc도 변경
old_desc_10 = r'<div class="desc">강자들은 당도, 선별, 선물 경험에서 이미 익숙한 문법을 갖고 있습니다\. 우리가 가져갈 축은 더 좋은 선물이 아니라 더 자주, 더 부담 없이, 더\s+실패 없이 먹게 만드는 환경입니다\.</div>'
new_desc_10 = '''<div class="desc">온브릭스는 당도 중심 프리미엄 전략으로 1,030억 누적 매출을 달성했으나, 정보 투명성·보장제 운영·타겟 단일화에서 약점을 보입니다. 우리는 이 3가지를 정면 공략합니다.</div>'''

content = re.sub(old_desc_10, new_desc_10, content)
print("✓ Slide #10 (now #12) enhanced (Onbricks 3 weaknesses)")

# ========================================
# 슬라이드 #17 (원래 #17, 지금은 #19) 보강: Phase 1/2 구체화
# ========================================
# 표 안의 내용을 더 구체적으로 수정
# "가족 루틴 랜딩 A/B" 행에 구체적 숫자 추가
old_exp_1 = r'<td>가족 루틴 랜딩 A/B</td>\s+<td>품종 중심 랜딩보다 `버리지 않는 가족 3일 과일 루틴` 랜딩이 상세 진입과 장바구니 진입을 더 만든다</td>'
new_exp_1 = '''<td>가족 루틴 랜딩 A/B (1개월, 1,000방문)</td>
                        <td>품종 중심 랜딩보다 '버리지 않는 가족 3일 과일 루틴' 랜딩이 상세 진입과 장바구니 진입을 더 만든다</td>'''

content = re.sub(old_exp_1, new_exp_1, content)
print("✓ Slide #17 (now #19) enhanced (Phase 1/2 details)")

# 저장
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n=== All enhancements completed ===")
print("File: strategy_a_proposal_v2.html")
