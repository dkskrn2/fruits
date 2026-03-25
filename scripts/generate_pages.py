#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import os
from pathlib import Path

# 기본 경로 설정
BASE_DIR = Path("C:/Users/dkskr/OneDrive/111/fruits")
OUTPUT_DIR = BASE_DIR / "output" / "pages"
TEMPLATE_DIR = BASE_DIR / "output" / "templates"
CSV_PATH = BASE_DIR / "output" / "ia_structure_enhanced.csv"

# 템플릿 읽기
def read_template():
    with open(TEMPLATE_DIR / "base_template.html", "r", encoding="utf-8") as f:
        return f.read()

# URL을 파일 경로로 변환
def url_to_filepath(url, page_name_en):
    """URL을 실제 파일 경로로 변환"""
    if url == "/":
        return OUTPUT_DIR / "home" / "index.html"

    # URL 파싱
    parts = url.strip("/").split("/")

    # 동적 URL 처리 ({id}, {name} 등)
    if "{" in url:
        # 동적 부분을 template로 대체
        filename = parts[-1].split("{")[0] + "template.html"
        folder = "/".join(parts[:-1])
        return OUTPUT_DIR / folder / filename

    # 일반 URL 처리
    if len(parts) == 1:
        # /cart, /event 등
        return OUTPUT_DIR / parts[0] / "index.html"
    elif len(parts) >= 2:
        # /products/all, /mypage/orders 등
        folder = parts[0]
        filename = parts[-1] + ".html"
        return OUTPUT_DIR / folder / filename

    return None

# 페이지별 헤더 컨텐츠 생성
def generate_header(page_name, url, depth1):
    """페이지별 헤더 생성"""
    if url == "/" or url == "/impact":
        # 홈 페이지는 로고만
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
        # 다른 페이지는 뒤로가기 + 타이틀
        return f'''
        <span class="header-back" onclick="history.back()">←</span>
        <h1 class="header-title">{page_name}</h1>
        <div class="header-actions">
            <span class="header-icon">🏠</span>
        </div>
        '''

# 페이지별 더미 콘텐츠 생성
def generate_content(page_name, url, description, functions, page_type):
    """페이지 타입별 더미 콘텐츠 생성"""

    # 기능 리스트 파싱
    function_list = functions.split(", ") if pd.notna(functions) else []

    # 페이지 타입별 콘텐츠
    if "목록" in page_name or "리스트" in description or "all" in url:
        # 리스트형 페이지
        content = f'''
        <div class="page-header">
            <h2>{page_name}</h2>
            <p class="page-desc">{description}</p>
        </div>

        <!-- 필터/정렬 -->
        <div class="filter-bar">
            <button class="filter-btn">필터</button>
            <button class="sort-btn">정렬</button>
        </div>

        <!-- 리스트 아이템 -->
        <div class="item-list">
        '''

        for i in range(5):
            content += f'''
            <div class="card list-item">
                <img src="https://via.placeholder.com/100" class="item-image" style="width: 100px; height: 100px; border-radius: 8px;">
                <div class="item-info" style="flex: 1; margin-left: 12px;">
                    <h3 class="item-title">샘플 아이템 {i+1}</h3>
                    <p class="item-desc">설명 텍스트가 들어갑니다</p>
                    <div class="item-price">25,000원</div>
                </div>
            </div>
            '''

        content += "</div>"

    elif "로그인" in page_name or "회원가입" in page_name or "문의" in page_name or "작성" in page_name:
        # 폼 페이지
        content = f'''
        <div class="page-header">
            <h2>{page_name}</h2>
            <p class="page-desc">{description}</p>
        </div>

        <form class="form-container">
        '''

        if "로그인" in page_name:
            content += '''
            <div class="form-group">
                <label class="form-label">아이디</label>
                <input type="text" class="form-input" placeholder="아이디를 입력하세요">
            </div>
            <div class="form-group">
                <label class="form-label">비밀번호</label>
                <input type="password" class="form-input" placeholder="비밀번호를 입력하세요">
            </div>
            <button type="button" class="button button-primary button-full">로그인</button>
            '''
        elif "회원가입" in page_name:
            content += '''
            <div class="form-group">
                <label class="form-label">이름</label>
                <input type="text" class="form-input" placeholder="이름을 입력하세요">
            </div>
            <div class="form-group">
                <label class="form-label">이메일</label>
                <input type="email" class="form-input" placeholder="이메일을 입력하세요">
            </div>
            <div class="form-group">
                <label class="form-label">휴대폰</label>
                <input type="tel" class="form-input" placeholder="010-0000-0000">
            </div>
            <div class="form-group">
                <label class="form-label">비밀번호</label>
                <input type="password" class="form-input" placeholder="비밀번호를 입력하세요">
            </div>
            <button type="button" class="button button-primary button-full">가입하기</button>
            '''
        else:
            # 일반 폼
            content += '''
            <div class="form-group">
                <label class="form-label">제목</label>
                <input type="text" class="form-input" placeholder="제목을 입력하세요">
            </div>
            <div class="form-group">
                <label class="form-label">내용</label>
                <textarea class="form-input" rows="5" placeholder="내용을 입력하세요"></textarea>
            </div>
            <button type="button" class="button button-primary button-full">제출</button>
            '''

        content += "</form>"

    elif "상세" in page_name or "detail" in url:
        # 상세 페이지
        content = f'''
        <div class="detail-container">
            <img src="https://via.placeholder.com/400x300" style="width: 100%; height: 300px; object-fit: cover;">

            <div class="detail-info" style="padding: 20px;">
                <h2>{page_name}</h2>
                <p class="page-desc">{description}</p>

                <div class="detail-content">
                    <p>상세 정보가 표시됩니다. 이미지 갤러리, 설명, 옵션 선택 등의 기능이 포함됩니다.</p>
                </div>

                <div class="action-buttons" style="margin-top: 20px;">
                    <button class="button button-secondary" style="width: 48%;">찜하기</button>
                    <button class="button button-primary" style="width: 48%;">구매하기</button>
                </div>
            </div>
        </div>
        '''

    elif "마이페이지" in page_name or "메인" in page_name or url == "/":
        # 대시보드형 페이지
        content = f'''
        <div class="dashboard">
            <h2>{page_name}</h2>
            <p class="page-desc">{description}</p>

            <!-- 요약 카드들 -->
            <div class="summary-cards" style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 20px 0;">
                <div class="card" style="text-align: center;">
                    <div style="font-size: 24px;">🎁</div>
                    <div style="font-size: 18px; font-weight: bold;">12</div>
                    <div style="font-size: 12px; color: var(--text-secondary);">진행중 주문</div>
                </div>
                <div class="card" style="text-align: center;">
                    <div style="font-size: 24px;">💰</div>
                    <div style="font-size: 18px; font-weight: bold;">5,000P</div>
                    <div style="font-size: 12px; color: var(--text-secondary);">포인트</div>
                </div>
                <div class="card" style="text-align: center;">
                    <div style="font-size: 24px;">🎫</div>
                    <div style="font-size: 18px; font-weight: bold;">3장</div>
                    <div style="font-size: 12px; color: var(--text-secondary);">쿠폰</div>
                </div>
                <div class="card" style="text-align: center;">
                    <div style="font-size: 24px;">❤️</div>
                    <div style="font-size: 18px; font-weight: bold;">8개</div>
                    <div style="font-size: 12px; color: var(--text-secondary);">찜</div>
                </div>
            </div>

            <!-- 메뉴 리스트 -->
            <div class="menu-list">
        '''

        # 주요 기능들을 메뉴로 표시
        for func in function_list[:6]:
            content += f'''
                <div class="card menu-item" style="display: flex; align-items: center; justify-content: space-between;">
                    <span>{func}</span>
                    <span>›</span>
                </div>
            '''

        content += '''
            </div>
        </div>
        '''

    else:
        # 정보형 페이지 (기본)
        content = f'''
        <div class="info-page">
            <h2>{page_name}</h2>
            <p class="page-desc">{description}</p>

            <div class="info-content" style="margin-top: 20px;">
        '''

        # 주요 기능들을 섹션으로 표시
        if function_list:
            content += '<h3 style="margin: 20px 0 10px;">주요 기능</h3><ul style="padding-left: 20px;">'
            for func in function_list:
                content += f'<li style="margin: 5px 0;">{func}</li>'
            content += '</ul>'

        content += '''
                <div class="card" style="margin: 20px 0;">
                    <p>이 페이지는 준비 중입니다. 곧 서비스를 제공할 예정입니다.</p>
                </div>
            </div>
        </div>
        '''

    return content

# 네비게이션 활성 상태 결정
def get_nav_active(depth1):
    """현재 페이지에 따른 네비게이션 활성 상태"""
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
    """각 페이지 HTML 생성"""
    # 데이터 추출
    page_name = row['페이지명_KO']
    page_name_en = row['페이지명_EN']
    url = row['URL']
    description = row['설명']
    depth1 = row['Depth1']
    functions = row['기능']
    status = row['상태']

    # 이미 완료된 페이지는 건너뛰기
    if status == "완료":
        print(f"  ⏭️  {page_name} - 이미 완료됨")
        return

    # 파일 경로 결정
    filepath = url_to_filepath(url, page_name_en)
    if not filepath:
        print(f"  ❌ {page_name} - 경로 변환 실패")
        return

    # 디렉토리 생성
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # 템플릿 치환
    html = template
    html = html.replace("{{PAGE_TITLE}}", page_name)
    html = html.replace("{{PAGE_STYLES}}", "")
    html = html.replace("{{HEADER_CONTENT}}", generate_header(page_name, url, depth1))
    html = html.replace("{{MAIN_CONTENT}}", generate_content(page_name, url, description, functions, ""))

    # 네비게이션 활성 상태
    nav_states = get_nav_active(depth1)
    for key, value in nav_states.items():
        html = html.replace("{{" + key + "}}", value)

    # 파일 저장
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"  ✅ {page_name} -> {filepath.relative_to(OUTPUT_DIR)}")

# 메인 실행 함수
def main():
    print("=" * 60)
    print("🚀 과일다리 페이지 생성 시작")
    print("=" * 60)

    # CSV 읽기
    print("\n📊 사이트맵 데이터 로딩...")
    df = pd.read_csv(CSV_PATH)
    print(f"  - 총 {len(df)}개 페이지 발견")

    # 템플릿 읽기
    print("\n📄 템플릿 로딩...")
    template = read_template()
    print("  - base_template.html 로드 완료")

    # 페이지 생성
    print("\n🔧 페이지 생성 중...")
    generated = 0
    skipped = 0

    for index, row in df.iterrows():
        if pd.notna(row['URL']) and row['URL'] != 'URL':  # 헤더 행 제외
            generate_page(row, template)
            if row['상태'] != "완료":
                generated += 1
            else:
                skipped += 1

    print("\n" + "=" * 60)
    print(f"✨ 페이지 생성 완료!")
    print(f"  - 생성: {generated}개")
    print(f"  - 건너뜀: {skipped}개")
    print(f"  - 위치: {OUTPUT_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()