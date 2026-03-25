#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import os
import sys
import random
from pathlib import Path
from datetime import datetime, timedelta

# UTF-8 인코딩 설정
sys.stdout.reconfigure(encoding='utf-8')

# 기본 경로 설정
BASE_DIR = Path("C:/Users/dkskr/OneDrive/111/fruits")
OUTPUT_DIR = BASE_DIR / "output" / "pages"
TEMPLATE_DIR = BASE_DIR / "output" / "templates"
CSV_PATH = BASE_DIR / "output" / "ia_structure_enhanced.csv"

# ===== 더미 데이터 정의 =====

# 과일 상품 데이터
FRUITS_DATA = [
    {"name": "제주 한라봉", "price": "32,000", "brix": "13.5", "origin": "제주도", "desc": "새콤달콤한 제주 특산품", "category": "seasonal"},
    {"name": "나주 배", "price": "28,000", "brix": "12.0", "origin": "전라남도 나주", "desc": "아삭하고 시원한 나주배", "category": "greeting"},
    {"name": "청송 사과", "price": "25,000", "brix": "14.0", "origin": "경상북도 청송", "desc": "달콤한 꿀사과", "category": "family"},
    {"name": "성주 참외", "price": "18,000", "brix": "11.5", "origin": "경상북도 성주", "desc": "여름 대표 과일", "category": "kids"},
    {"name": "담양 딸기", "price": "15,000", "brix": "10.0", "origin": "전라남도 담양", "desc": "새콤달콤 딸기", "category": "kids"},
    {"name": "영동 포도", "price": "22,000", "brix": "16.0", "origin": "충청북도 영동", "desc": "당도 높은 샤인머스켓", "category": "family"},
    {"name": "제주 감귤", "price": "20,000", "brix": "11.0", "origin": "제주도", "desc": "비타민C 가득", "category": "donation"},
    {"name": "무주 복숭아", "price": "30,000", "brix": "13.0", "origin": "전라북도 무주", "desc": "향긋한 백도 복숭아", "category": "seasonal"},
]

# 주문 내역 데이터
ORDERS_DATA = [
    {"order_no": "20241215001", "date": "2024.12.15", "products": "제주 한라봉 외 2건", "amount": "75,000원", "status": "배송완료"},
    {"order_no": "20241210002", "date": "2024.12.10", "products": "나주 배 세트", "amount": "56,000원", "status": "배송중"},
    {"order_no": "20241205003", "date": "2024.12.05", "products": "과일 정기배송 12월", "amount": "120,000원", "status": "배송준비"},
]

# 이벤트 데이터
EVENTS_DATA = [
    {"title": "12월 연말 감사 이벤트", "period": "2024.12.01 - 12.31", "desc": "구매금액의 10% 포인트 적립", "status": "진행중"},
    {"title": "신규회원 50% 할인", "period": "2024.12.01 - 12.31", "desc": "첫 구매시 최대 5만원 할인", "status": "진행중"},
    {"title": "과일다리 1주년 기념", "period": "2024.11.01 - 11.30", "desc": "전 상품 20% 할인", "status": "종료"},
]

# FAQ 데이터
FAQ_DATA = [
    {"q": "배송은 얼마나 걸리나요?", "a": "주문 후 1-2일 내 신선하게 배송됩니다. 제주/도서지역은 추가 1일이 소요될 수 있습니다."},
    {"q": "Brix 당도는 무엇인가요?", "a": "Brix는 과일의 당도를 측정하는 단위입니다. 숫자가 높을수록 더 달콤합니다."},
    {"q": "교환/반품이 가능한가요?", "a": "상품 수령 후 24시간 이내 신선도 문제 발생시 100% 교환/환불 가능합니다."},
    {"q": "정기배송 해지는 어떻게 하나요?", "a": "마이페이지 > 정기배송 관리에서 언제든지 해지 가능합니다."},
    {"q": "나눔 과일은 어떻게 기부되나요?", "a": "구매금액의 일부가 자동으로 적립되어 월 1회 지역 복지시설에 과일을 기부합니다."},
]

# 공지사항 데이터
NOTICE_DATA = [
    {"title": "[공지] 12월 배송 일정 안내", "date": "2024.12.15", "important": True},
    {"title": "[이벤트] 연말 감사 이벤트 당첨자 발표", "date": "2024.12.10", "important": False},
    {"title": "[안내] 개인정보처리방침 개정 안내", "date": "2024.12.05", "important": False},
    {"title": "[공지] 시스템 점검 안내 (12/20)", "date": "2024.12.01", "important": True},
]

# 템플릿 읽기
def read_template():
    with open(TEMPLATE_DIR / "base_template.html", "r", encoding="utf-8") as f:
        return f.read()

# URL을 파일 경로로 변환
def url_to_filepath(url, page_name_en):
    """URL을 실제 파일 경로로 변환"""
    if url == "/":
        return OUTPUT_DIR / "home" / "index.html"

    parts = url.strip("/").split("/")

    if "{" in url:
        filename = parts[-1].split("{")[0] + "template.html"
        folder = "/".join(parts[:-1])
        return OUTPUT_DIR / folder / filename

    if len(parts) == 1:
        return OUTPUT_DIR / parts[0] / "index.html"
    elif len(parts) >= 2:
        folder = parts[0]
        filename = parts[-1] + ".html"
        return OUTPUT_DIR / folder / filename

    return None

# 페이지별 헤더 생성
def generate_header(page_name, url, depth1):
    """페이지별 헤더 생성"""
    if url == "/" or url == "/impact":
        return '''
        <a href="index.html" class="logo">
            <span class="fruit">과일</span>
            <span class="bridge">다리</span>
        </a>
        <div class="header-actions">
            <span class="header-icon">🔍</span>
            <span class="header-icon">🛒</span>
        </div>
        '''
    else:
        return f'''
        <span class="header-back" onclick="history.back()">←</span>
        <h1 class="header-title">{page_name}</h1>
        <div class="header-actions">
            <span class="header-icon">🏠</span>
        </div>
        '''

# 강화된 콘텐츠 생성 함수
def generate_enhanced_content(page_name, url, description, functions):
    """페이지별 맞춤 콘텐츠 생성"""

    # === 상품 카테고리 페이지 ===
    if any(cat in url for cat in ["family", "kids", "greeting", "donation", "seasonal", "best", "new"]):
        content = f'''
        <div class="page-header">
            <h2>{page_name}</h2>
            <p class="page-desc">{description}</p>
        </div>

        <div class="filter-bar" style="display: flex; gap: 10px; margin: 15px 0;">
            <button style="padding: 8px 16px; border: 1px solid var(--border); border-radius: 20px; background: white;">가격순</button>
            <button style="padding: 8px 16px; border: 1px solid var(--border); border-radius: 20px; background: white;">당도순</button>
            <button style="padding: 8px 16px; border: 1px solid var(--border); border-radius: 20px; background: white;">인기순</button>
        </div>

        <div class="products-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
        '''

        # 카테고리별 과일 필터링
        category_fruits = [f for f in FRUITS_DATA if url.split("/")[-1] in f.get("category", "")]
        if not category_fruits:
            category_fruits = random.sample(FRUITS_DATA, min(6, len(FRUITS_DATA)))

        for fruit in category_fruits[:6]:
            content += f'''
            <div class="product-card" style="background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <div style="height: 120px; background: linear-gradient(135deg, #FFE0B2, #FFCC80); display: flex; align-items: center; justify-content: center; font-size: 48px;">
                    🍊
                </div>
                <div style="padding: 12px;">
                    <h4 style="font-size: 14px; margin-bottom: 4px;">{fruit['name']}</h4>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-bottom: 8px;">{fruit['desc']}</p>
                    <div style="display: flex; align-items: center; gap: 4px; margin-bottom: 8px;">
                        <span style="background: #FFF3E0; color: #E65100; padding: 2px 6px; border-radius: 4px; font-size: 10px;">당도 {fruit['brix']}°</span>
                        <span style="font-size: 10px; color: var(--text-muted);">{fruit['origin']}</span>
                    </div>
                    <div style="font-weight: bold; color: var(--primary-green); margin-bottom: 8px;">{fruit['price']}원</div>
                    <button style="width: 100%; padding: 8px; background: var(--primary-green); color: white; border: none; border-radius: 6px; font-size: 12px;">장바구니</button>
                </div>
            </div>
            '''

        content += '</div>'

    # === 장바구니 페이지 ===
    elif url == "/cart":
        content = f'''
        <div class="page-header">
            <h2>{page_name}</h2>
            <p class="page-desc">{description}</p>
        </div>

        <div class="cart-items">
        '''

        for i, fruit in enumerate(random.sample(FRUITS_DATA, 3)):
            quantity = random.randint(1, 3)
            price = int(fruit['price'].replace(",", ""))
            total = price * quantity
            content += f'''
            <div class="card" style="margin-bottom: 12px;">
                <div style="display: flex; align-items: center;">
                    <input type="checkbox" checked style="margin-right: 12px;">
                    <div style="width: 60px; height: 60px; background: #FFE0B2; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-right: 12px;">
                        🍎
                    </div>
                    <div style="flex: 1;">
                        <h4 style="font-size: 14px;">{fruit['name']}</h4>
                        <p style="font-size: 12px; color: var(--text-secondary);">{fruit['origin']}</p>
                    </div>
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <button style="width: 24px; height: 24px; border: 1px solid var(--border); background: white; border-radius: 4px;">-</button>
                        <span style="font-size: 14px;">{quantity}</span>
                        <button style="width: 24px; height: 24px; border: 1px solid var(--border); background: white; border-radius: 4px;">+</button>
                    </div>
                    <div style="text-align: right; margin-left: 16px;">
                        <div style="font-weight: bold;">{total:,}원</div>
                    </div>
                </div>
            </div>
            '''

        content += f'''
        </div>

        <div class="card" style="margin: 20px 0; background: var(--bg-gray);">
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                <span>상품금액</span>
                <span>83,000원</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                <span>배송비</span>
                <span>무료</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-weight: bold; font-size: 18px; padding-top: 12px; border-top: 1px solid var(--border);">
                <span>총 결제금액</span>
                <span style="color: var(--primary-green);">83,000원</span>
            </div>
        </div>

        <button class="button button-primary button-full">주문하기</button>
        '''

    # === 주문내역 페이지 ===
    elif "orders" in url or "주문내역" in page_name:
        content = f'''
        <div class="page-header">
            <h2>{page_name}</h2>
            <p class="page-desc">{description}</p>
        </div>

        <div class="order-list">
        '''

        for order in ORDERS_DATA:
            status_color = "#4CAF50" if order['status'] == "배송완료" else "#FF9800"
            content += f'''
            <div class="card" style="margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                    <span style="font-size: 12px; color: var(--text-secondary);">{order['date']}</span>
                    <span style="font-size: 11px; padding: 2px 8px; background: {status_color}20; color: {status_color}; border-radius: 4px;">{order['status']}</span>
                </div>
                <h4 style="font-size: 14px; margin-bottom: 4px;">주문번호: {order['order_no']}</h4>
                <p style="font-size: 13px; margin-bottom: 8px;">{order['products']}</p>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: bold; color: var(--primary-green);">{order['amount']}</span>
                    <button style="padding: 6px 12px; border: 1px solid var(--border); background: white; border-radius: 4px; font-size: 12px;">상세보기</button>
                </div>
            </div>
            '''

        content += '</div>'

    # === 이벤트 페이지 ===
    elif "event" in url:
        status_filter = "ongoing" if "ongoing" in url else "ended" if "ended" in url else None
        content = f'''
        <div class="page-header">
            <h2>{page_name}</h2>
            <p class="page-desc">{description}</p>
        </div>

        <div class="event-list">
        '''

        events = [e for e in EVENTS_DATA if not status_filter or (status_filter == "ongoing" and e['status'] == "진행중") or (status_filter == "ended" and e['status'] == "종료")]

        for event in events:
            badge_color = "#4CAF50" if event['status'] == "진행중" else "#9E9E9E"
            content += f'''
            <div class="card" style="margin-bottom: 12px; overflow: hidden;">
                <div style="height: 120px; background: linear-gradient(135deg, #8BC34A, #689F38); display: flex; align-items: center; justify-content: center; color: white; font-size: 48px;">
                    🎉
                </div>
                <div style="padding: 16px;">
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;">
                        <h3 style="font-size: 16px; flex: 1;">{event['title']}</h3>
                        <span style="font-size: 11px; padding: 4px 8px; background: {badge_color}; color: white; border-radius: 4px;">{event['status']}</span>
                    </div>
                    <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 8px;">{event['desc']}</p>
                    <p style="font-size: 12px; color: var(--text-muted);">기간: {event['period']}</p>
                    <button style="width: 100%; padding: 10px; margin-top: 12px; background: var(--primary-green); color: white; border: none; border-radius: 6px;">자세히 보기</button>
                </div>
            </div>
            '''

        content += '</div>'

    # === FAQ 페이지 ===
    elif "faq" in url:
        content = f'''
        <div class="page-header">
            <h2>{page_name}</h2>
            <p class="page-desc">{description}</p>
        </div>

        <div class="faq-categories" style="display: flex; gap: 8px; margin: 20px 0; overflow-x: auto;">
            <button style="padding: 8px 16px; background: var(--primary-green); color: white; border: none; border-radius: 20px; white-space: nowrap;">전체</button>
            <button style="padding: 8px 16px; background: white; border: 1px solid var(--border); border-radius: 20px; white-space: nowrap;">배송</button>
            <button style="padding: 8px 16px; background: white; border: 1px solid var(--border); border-radius: 20px; white-space: nowrap;">주문/결제</button>
            <button style="padding: 8px 16px; background: white; border: 1px solid var(--border); border-radius: 20px; white-space: nowrap;">교환/반품</button>
        </div>

        <div class="faq-list">
        '''

        for i, faq in enumerate(FAQ_DATA):
            content += f'''
            <div class="card" style="margin-bottom: 12px;">
                <div style="cursor: pointer;" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'none' ? 'block' : 'none'">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span style="color: var(--primary-green); font-weight: bold;">Q</span>
                            <span style="font-size: 14px;">{faq['q']}</span>
                        </div>
                        <span style="font-size: 20px;">›</span>
                    </div>
                </div>
                <div style="display: none; margin-top: 12px; padding-top: 12px; border-top: 1px solid var(--border);">
                    <div style="display: flex; gap: 8px;">
                        <span style="color: var(--primary-green); font-weight: bold;">A</span>
                        <p style="font-size: 13px; color: var(--text-secondary); line-height: 1.6;">{faq['a']}</p>
                    </div>
                </div>
            </div>
            '''

        content += '</div>'

    # === 공지사항 페이지 ===
    elif "notice" in url:
        content = f'''
        <div class="page-header">
            <h2>{page_name}</h2>
            <p class="page-desc">{description}</p>
        </div>

        <div class="notice-list">
        '''

        for notice in NOTICE_DATA:
            icon = "📌" if notice['important'] else "📄"
            content += f'''
            <div class="card" style="margin-bottom: 12px; cursor: pointer;">
                <div style="display: flex; align-items: start; gap: 12px;">
                    <span style="font-size: 20px;">{icon}</span>
                    <div style="flex: 1;">
                        <h4 style="font-size: 14px; margin-bottom: 4px;">{notice['title']}</h4>
                        <span style="font-size: 12px; color: var(--text-muted);">{notice['date']}</span>
                    </div>
                    <span style="font-size: 18px; color: var(--text-muted);">›</span>
                </div>
            </div>
            '''

        content += '</div>'

    # === 포인트 페이지 ===
    elif "points" in url or "포인트" in page_name:
        content = f'''
        <div class="page-header">
            <h2>{page_name}</h2>
            <p class="page-desc">{description}</p>
        </div>

        <div class="card" style="background: linear-gradient(135deg, #8BC34A, #689F38); color: white; margin-bottom: 20px;">
            <div style="text-align: center; padding: 20px;">
                <p style="font-size: 14px; opacity: 0.9;">사용 가능 포인트</p>
                <p style="font-size: 32px; font-weight: bold; margin: 8px 0;">5,280 P</p>
                <p style="font-size: 12px; opacity: 0.9;">이번달 소멸예정: 500P</p>
            </div>
        </div>

        <div class="point-history">
            <h3 style="font-size: 16px; margin-bottom: 12px;">포인트 내역</h3>
        '''

        point_history = [
            {"date": "2024.12.15", "desc": "제주 한라봉 구매 적립", "point": "+320", "type": "적립"},
            {"date": "2024.12.10", "desc": "포인트 사용", "point": "-1,000", "type": "사용"},
            {"date": "2024.12.05", "desc": "리뷰 작성 적립", "point": "+100", "type": "적립"},
            {"date": "2024.12.01", "desc": "12월 등급 보너스", "point": "+500", "type": "적립"},
        ]

        for item in point_history:
            color = "var(--primary-green)" if item['type'] == "적립" else "var(--red)"
            content += f'''
            <div class="card" style="margin-bottom: 8px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <p style="font-size: 13px; margin-bottom: 4px;">{item['desc']}</p>
                        <span style="font-size: 11px; color: var(--text-muted);">{item['date']}</span>
                    </div>
                    <span style="font-weight: bold; color: {color};">{item['point']}P</span>
                </div>
            </div>
            '''

        content += '</div>'

    # === 쿠폰함 페이지 ===
    elif "coupon" in url or "쿠폰" in page_name:
        content = f'''
        <div class="page-header">
            <h2>{page_name}</h2>
            <p class="page-desc">{description}</p>
        </div>

        <div class="tabs" style="display: flex; border-bottom: 1px solid var(--border); margin-bottom: 20px;">
            <button style="flex: 1; padding: 12px; border: none; background: none; border-bottom: 2px solid var(--primary-green); color: var(--primary-green);">사용가능 (3)</button>
            <button style="flex: 1; padding: 12px; border: none; background: none; color: var(--text-muted);">사용완료 (2)</button>
        </div>

        <div class="coupon-list">
        '''

        coupons = [
            {"title": "신규회원 50% 할인", "desc": "최대 5만원 할인", "expire": "2024.12.31", "min": "3만원 이상"},
            {"title": "12월 특별 할인 20%", "desc": "전 상품 적용", "expire": "2024.12.31", "min": "5만원 이상"},
            {"title": "무료배송 쿠폰", "desc": "배송비 무료", "expire": "2024.12.25", "min": "2만원 이상"},
        ]

        for coupon in coupons:
            content += f'''
            <div class="card" style="margin-bottom: 12px; border: 2px dashed var(--primary-green); background: #F1F8E9;">
                <div style="display: flex; align-items: center;">
                    <div style="width: 80px; text-align: center; padding: 16px; border-right: 1px dashed var(--primary-green);">
                        <div style="font-size: 24px; color: var(--primary-green); font-weight: bold;">SALE</div>
                    </div>
                    <div style="flex: 1; padding: 16px;">
                        <h4 style="font-size: 14px; margin-bottom: 4px;">{coupon['title']}</h4>
                        <p style="font-size: 12px; color: var(--text-secondary); margin-bottom: 4px;">{coupon['desc']}</p>
                        <div style="font-size: 11px; color: var(--text-muted);">
                            <span>최소주문: {coupon['min']}</span> |
                            <span>~{coupon['expire']}까지</span>
                        </div>
                    </div>
                    <button style="padding: 8px 16px; background: var(--primary-green); color: white; border: none; border-radius: 4px; margin-right: 16px;">사용</button>
                </div>
            </div>
            '''

        content += '</div>'

    # === 로그인 페이지 (기존 유지) ===
    elif "로그인" in page_name:
        content = f'''
        <div style="text-align: center; padding: 40px 20px;">
            <h1 style="color: var(--primary-green); font-size: 28px; margin-bottom: 8px;">과일다리</h1>
            <p style="color: var(--text-secondary); font-size: 14px; margin-bottom: 40px;">건강을 잇는 다리</p>
        </div>

        <form class="form-container" style="padding: 0 20px;">
            <div class="form-group">
                <input type="text" class="form-input" placeholder="아이디" style="padding: 14px;">
            </div>
            <div class="form-group">
                <input type="password" class="form-input" placeholder="비밀번호" style="padding: 14px;">
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <label style="display: flex; align-items: center; font-size: 14px;">
                    <input type="checkbox" style="margin-right: 8px;"> 자동 로그인
                </label>
                <a href="#" style="font-size: 14px; color: var(--text-secondary); text-decoration: none;">아이디/비밀번호 찾기</a>
            </div>

            <button type="button" class="button button-primary button-full" style="margin-bottom: 12px;">로그인</button>
            <button type="button" class="button button-secondary button-full">회원가입</button>

            <div style="text-align: center; margin: 30px 0;">
                <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 16px;">간편 로그인</p>
                <div style="display: flex; justify-content: center; gap: 16px;">
                    <button style="width: 48px; height: 48px; border-radius: 50%; background: #FEE500; border: none; font-size: 20px;">K</button>
                    <button style="width: 48px; height: 48px; border-radius: 50%; background: #03C75A; border: none; color: white; font-size: 20px;">N</button>
                    <button style="width: 48px; height: 48px; border-radius: 50%; background: #4285F4; border: none; color: white; font-size: 20px;">G</button>
                </div>
            </div>
        </form>
        '''

    # === 회원가입 페이지 (개선) ===
    elif "회원가입" in page_name or "signup" in url:
        content = f'''
        <div class="page-header" style="text-align: center;">
            <h2>{page_name}</h2>
            <p class="page-desc">과일다리 회원이 되어 특별한 혜택을 받아보세요</p>
        </div>

        <form class="form-container">
            <div class="form-group">
                <label class="form-label">이름 <span style="color: red;">*</span></label>
                <input type="text" class="form-input" placeholder="실명을 입력해주세요">
            </div>

            <div class="form-group">
                <label class="form-label">아이디 <span style="color: red;">*</span></label>
                <div style="display: flex; gap: 8px;">
                    <input type="text" class="form-input" placeholder="4-20자 영문, 숫자" style="flex: 1;">
                    <button type="button" style="padding: 0 16px; border: 1px solid var(--primary-green); color: var(--primary-green); background: white; border-radius: 6px;">중복확인</button>
                </div>
            </div>

            <div class="form-group">
                <label class="form-label">비밀번호 <span style="color: red;">*</span></label>
                <input type="password" class="form-input" placeholder="8자 이상 영문, 숫자, 특수문자 조합">
                <div style="margin-top: 8px;">
                    <div style="height: 4px; background: var(--border); border-radius: 2px;">
                        <div style="width: 30%; height: 100%; background: var(--orange); border-radius: 2px;"></div>
                    </div>
                    <span style="font-size: 11px; color: var(--orange);">보안 강도: 약함</span>
                </div>
            </div>

            <div class="form-group">
                <label class="form-label">비밀번호 확인 <span style="color: red;">*</span></label>
                <input type="password" class="form-input" placeholder="비밀번호를 다시 입력해주세요">
            </div>

            <div class="form-group">
                <label class="form-label">이메일 <span style="color: red;">*</span></label>
                <input type="email" class="form-input" placeholder="example@email.com">
            </div>

            <div class="form-group">
                <label class="form-label">휴대폰 <span style="color: red;">*</span></label>
                <div style="display: flex; gap: 8px;">
                    <input type="tel" class="form-input" placeholder="010-0000-0000" style="flex: 1;">
                    <button type="button" style="padding: 0 16px; border: 1px solid var(--primary-green); color: var(--primary-green); background: white; border-radius: 6px;">인증번호</button>
                </div>
            </div>

            <div class="form-group" style="margin-top: 30px;">
                <div style="padding: 16px; background: var(--bg-gray); border-radius: 8px;">
                    <label style="display: flex; align-items: start; margin-bottom: 12px;">
                        <input type="checkbox" style="margin-right: 8px; margin-top: 2px;">
                        <span style="font-size: 14px;"><strong>[필수]</strong> 이용약관 동의</span>
                    </label>
                    <label style="display: flex; align-items: start; margin-bottom: 12px;">
                        <input type="checkbox" style="margin-right: 8px; margin-top: 2px;">
                        <span style="font-size: 14px;"><strong>[필수]</strong> 개인정보 수집 및 이용 동의</span>
                    </label>
                    <label style="display: flex; align-items: start;">
                        <input type="checkbox" style="margin-right: 8px; margin-top: 2px;">
                        <span style="font-size: 14px;">[선택] 마케팅 정보 수신 동의</span>
                    </label>
                </div>
            </div>

            <button type="button" class="button button-primary button-full" style="margin-top: 20px;">가입하기</button>
        </form>
        '''

    # === 기본 정보형 페이지 (약관, 가이드 등) ===
    else:
        # 페이지별 맞춤 콘텐츠
        if "privacy" in url or "개인정보" in page_name:
            content = f'''
            <div class="page-header">
                <h2>{page_name}</h2>
                <p class="page-desc">시행일: 2024년 1월 1일</p>
            </div>

            <div class="terms-content" style="line-height: 1.8; font-size: 14px;">
                <h3 style="margin: 20px 0 12px;">제1조 (개인정보의 수집 및 이용목적)</h3>
                <p style="margin-bottom: 16px;">과일다리는 다음과 같은 목적을 위해 개인정보를 수집하고 이용합니다.</p>
                <ul style="padding-left: 20px; margin-bottom: 16px;">
                    <li>서비스 제공 및 계약 이행</li>
                    <li>회원 관리 및 본인 확인</li>
                    <li>마케팅 및 광고 활용</li>
                    <li>서비스 개선 및 신규 서비스 개발</li>
                </ul>

                <h3 style="margin: 20px 0 12px;">제2조 (수집하는 개인정보 항목)</h3>
                <p style="margin-bottom: 16px;">필수 항목: 이름, 아이디, 비밀번호, 이메일, 휴대폰번호, 배송지 정보</p>
                <p style="margin-bottom: 16px;">선택 항목: 생년월일, 성별, 관심 과일</p>

                <h3 style="margin: 20px 0 12px;">제3조 (개인정보의 보유 및 이용기간)</h3>
                <p style="margin-bottom: 16px;">회원 탈퇴 시까지 (단, 관련 법령에 따라 일정 기간 보관)</p>
            </div>
            '''

        elif "terms" in url or "이용약관" in page_name:
            content = f'''
            <div class="page-header">
                <h2>{page_name}</h2>
                <p class="page-desc">시행일: 2024년 1월 1일</p>
            </div>

            <div class="terms-content" style="line-height: 1.8; font-size: 14px;">
                <h3 style="margin: 20px 0 12px;">제1장 총칙</h3>

                <h4 style="margin: 16px 0 8px;">제1조 (목적)</h4>
                <p style="margin-bottom: 16px;">이 약관은 과일다리(이하 "회사")가 제공하는 전자상거래 서비스 이용과 관련하여 회사와 이용자의 권리, 의무 및 책임사항을 규정함을 목적으로 합니다.</p>

                <h4 style="margin: 16px 0 8px;">제2조 (정의)</h4>
                <p style="margin-bottom: 16px;">① "과일다리"란 회사가 재화 또는 용역을 이용자에게 제공하기 위하여 컴퓨터 등 정보통신설비를 이용하여 재화 등을 거래할 수 있도록 설정한 가상의 영업장을 말합니다.</p>
                <p style="margin-bottom: 16px;">② "이용자"란 "과일다리"에 접속하여 이 약관에 따라 "과일다리"가 제공하는 서비스를 받는 회원 및 비회원을 말합니다.</p>

                <h3 style="margin: 20px 0 12px;">제2장 서비스 이용</h3>

                <h4 style="margin: 16px 0 8px;">제3조 (회원가입)</h4>
                <p style="margin-bottom: 16px;">① 이용자는 과일다리가 정한 가입 양식에 따라 회원정보를 기입한 후 이 약관에 동의한다는 의사표시를 함으로서 회원가입을 신청합니다.</p>
            </div>
            '''

        elif "배송" in page_name or "delivery" in url:
            content = f'''
            <div class="page-header">
                <h2>{page_name}</h2>
                <p class="page-desc">{description}</p>
            </div>

            <div class="info-content">
                <div class="card" style="margin-bottom: 16px;">
                    <h3 style="font-size: 16px; margin-bottom: 12px;">🚚 배송 안내</h3>
                    <div style="font-size: 14px; line-height: 1.8;">
                        <p style="margin-bottom: 12px;"><strong>배송 지역:</strong> 전국 (일부 도서산간 지역 제외)</p>
                        <p style="margin-bottom: 12px;"><strong>배송 기간:</strong> 주문 후 1-2일 (영업일 기준)</p>
                        <p style="margin-bottom: 12px;"><strong>배송비:</strong> 3만원 이상 무료배송 / 3만원 미만 3,000원</p>
                        <p style="margin-bottom: 12px;"><strong>배송업체:</strong> CJ대한통운</p>
                    </div>
                </div>

                <div class="card" style="margin-bottom: 16px;">
                    <h3 style="font-size: 16px; margin-bottom: 12px;">📦 포장 안내</h3>
                    <p style="font-size: 14px; line-height: 1.6;">신선도 유지를 위해 특수 제작된 친환경 박스와 아이스팩으로 안전하게 포장하여 배송됩니다.</p>
                </div>

                <div class="card">
                    <h3 style="font-size: 16px; margin-bottom: 12px;">⚠️ 주의사항</h3>
                    <ul style="font-size: 14px; line-height: 1.8; padding-left: 20px;">
                        <li>신선식품 특성상 배송 후 재배송이 어려울 수 있습니다</li>
                        <li>배송일 지정은 주문 시 요청사항에 기재해주세요</li>
                        <li>제주 및 도서지역은 추가 1-2일 소요됩니다</li>
                    </ul>
                </div>
            </div>
            '''

        else:
            # 기본 정보 페이지
            content = f'''
            <div class="page-header">
                <h2>{page_name}</h2>
                <p class="page-desc">{description}</p>
            </div>

            <div class="info-content" style="margin-top: 20px;">
                <div class="card" style="padding: 24px; text-align: center;">
                    <div style="font-size: 48px; margin-bottom: 16px;">🍎</div>
                    <h3 style="font-size: 18px; margin-bottom: 12px;">{page_name}</h3>
                    <p style="font-size: 14px; color: var(--text-secondary); line-height: 1.6;">
                        {description}
                    </p>

                    <div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid var(--border);">
                        <p style="font-size: 13px; color: var(--text-muted);">
                            과일다리는 신선한 과일을 통해 건강한 삶을 지원합니다.<br>
                            문의사항이 있으시면 고객센터로 연락 주세요.
                        </p>
                        <div style="margin-top: 16px;">
                            <button class="button button-primary">고객센터 바로가기</button>
                        </div>
                    </div>
                </div>
            </div>
            '''

    return content

# 네비게이션 활성 상태
def get_nav_active(depth1):
    nav_states = {
        "HOME_ACTIVE": "",
        "PRODUCTS_ACTIVE": "",
        "MYPAGE_ACTIVE": "",
        "SUPPORT_ACTIVE": ""
    }

    if depth1 == "홈":
        nav_states["HOME_ACTIVE"] = "active"
    elif depth1 == "상품":
        nav_states["PRODUCTS_ACTIVE"] = "active"
    elif depth1 == "마이페이지":
        nav_states["MYPAGE_ACTIVE"] = "active"
    elif depth1 == "고객지원":
        nav_states["SUPPORT_ACTIVE"] = "active"

    return nav_states

# 페이지 생성 함수
def generate_page(row, template):
    page_name = row['페이지명_KO']
    url = row['URL']
    description = row['설명']
    depth1 = row['Depth1']
    functions = row['기능']
    status = row['상태']

    if status == "완료":
        print(f"  ⏭️  {page_name} - 이미 완료됨")
        return False

    filepath = url_to_filepath(url, row['페이지명_EN'])
    if not filepath:
        print(f"  ❌ {page_name} - 경로 변환 실패")
        return False

    filepath.parent.mkdir(parents=True, exist_ok=True)

    # 강화된 콘텐츠 생성
    html = template
    html = html.replace("{{PAGE_TITLE}}", page_name)
    html = html.replace("{{PAGE_STYLES}}", "")
    html = html.replace("{{HEADER_CONTENT}}", generate_header(page_name, url, depth1))
    html = html.replace("{{MAIN_CONTENT}}", generate_enhanced_content(page_name, url, description, functions))

    nav_states = get_nav_active(depth1)
    for key, value in nav_states.items():
        html = html.replace("{{" + key + "}}", value)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"  ✅ {page_name} -> {filepath.relative_to(OUTPUT_DIR)}")
    return True

# 메인 실행
def main():
    print("=" * 60)
    print("🚀 과일다리 페이지 콘텐츠 보완")
    print("=" * 60)

    print("\n📊 사이트맵 데이터 로딩...")
    df = pd.read_csv(CSV_PATH)
    print(f"  - 총 {len(df)}개 페이지 발견")

    print("\n📄 템플릿 로딩...")
    template = read_template()
    print("  - base_template.html 로드 완료")

    print("\n🔧 강화된 콘텐츠로 페이지 재생성...")
    updated = 0
    skipped = 0

    for index, row in df.iterrows():
        if pd.notna(row['URL']) and row['URL'] != 'URL':
            if generate_page(row, template):
                updated += 1
            else:
                skipped += 1

    print("\n" + "=" * 60)
    print(f"✨ 페이지 보완 완료!")
    print(f"  - 업데이트: {updated}개")
    print(f"  - 건너뜀: {skipped}개")
    print("=" * 60)

if __name__ == "__main__":
    main()