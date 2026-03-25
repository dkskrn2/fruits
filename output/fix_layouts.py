#!/usr/bin/env python3
"""
레이아웃 수정 스크립트
모든 HTML 파일에 layout-fix.css를 추가하여 레이아웃 문제 해결
"""

import os
import re
from pathlib import Path

# 경로 설정
BASE_DIR = Path(".")
PAGES_DIR = BASE_DIR / "pages"

def add_layout_fix_to_html(file_path):
    """HTML 파일에 layout-fix.css 추가"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 이미 layout-fix.css가 포함되어 있는지 확인
    if 'layout-fix.css' in content:
        return False

    # components.css 다음에 layout-fix.css 추가
    pattern = r'(<link rel="stylesheet" href="[^"]*components\.css">)'
    replacement = r'\1\n    <link rel="stylesheet" href="../../styles/layout-fix.css">'

    new_content = re.sub(pattern, replacement, content)

    # 변경사항이 있으면 저장
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False

def process_all_html_files():
    """모든 HTML 파일 처리"""
    updated_count = 0
    total_count = 0

    # pages 디렉토리의 모든 HTML 파일 찾기
    for html_file in PAGES_DIR.rglob("*.html"):
        total_count += 1
        if add_layout_fix_to_html(html_file):
            updated_count += 1
            print(f"[OK] Updated: {html_file.relative_to(BASE_DIR)}")
        else:
            print(f"[--] Skipped: {html_file.relative_to(BASE_DIR)} (already has layout-fix.css)")

    print("\n" + "=" * 60)
    print(f"Layout fix complete!")
    print(f"Updated {updated_count} of {total_count} files")
    print("=" * 60)

    return updated_count

def create_test_page():
    """레이아웃 테스트 페이지 생성"""
    test_html = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>레이아웃 수정 테스트 - 과일다리</title>
    <link rel="stylesheet" href="styles/design-system.css">
    <link rel="stylesheet" href="styles/components.css">
    <link rel="stylesheet" href="styles/layout-fix.css">
</head>
<body>
    <div class="auth-container">
        <header class="auth-header">
            <button class="btn-icon">✕</button>
            <h2 style="flex: 1; text-align: center;">레이아웃 테스트</h2>
            <button class="btn-icon">⚙️</button>
        </header>

        <div class="auth-logo-section">
            <div class="auth-logo">🍊</div>
            <h1 class="auth-brand-name">과일다리</h1>
            <p class="auth-brand-tagline">레이아웃이 정상적으로 표시됩니다</p>
        </div>

        <div class="auth-form">
            <div class="card mb-4">
                <div class="card-header">
                    <h3>카드 헤더</h3>
                </div>
                <div class="card-body">
                    <p>레이아웃 수정이 적용된 카드입니다.</p>
                    <div class="field mt-3">
                        <input type="text" class="control" placeholder="입력 필드 테스트">
                    </div>
                    <button class="btn btn-primary btn-full mt-3">전체 너비 버튼</button>
                </div>
            </div>

            <div class="grid">
                <div class="col-6">
                    <div class="product-card">
                        <div class="product-image" style="background: linear-gradient(135deg, #7AA37A, #E7A98D); display: grid; place-items: center; color: white; font-size: 48px;">🍎</div>
                        <div class="product-info">
                            <div class="product-name">신선한 사과</div>
                            <div class="product-price">5,900원</div>
                        </div>
                    </div>
                </div>
                <div class="col-6">
                    <div class="product-card">
                        <div class="product-image" style="background: linear-gradient(135deg, #E7A98D, #D8B36A); display: grid; place-items: center; color: white; font-size: 48px;">🍊</div>
                        <div class="product-info">
                            <div class="product-name">제주 감귤</div>
                            <div class="product-price">8,900원</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="bottom-nav">
            <div class="nav-item active">
                <div class="nav-icon">🏠</div>
                <div class="nav-label">홈</div>
            </div>
            <div class="nav-item">
                <div class="nav-icon">🛒</div>
                <div class="nav-label">장바구니</div>
            </div>
            <div class="nav-item">
                <div class="nav-icon">👤</div>
                <div class="nav-label">마이페이지</div>
            </div>
        </div>
    </div>
</body>
</html>"""

    test_file = BASE_DIR / "layout_test.html"
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(test_html)

    print(f"\n✨ 테스트 페이지 생성: {test_file}")
    print("   브라우저에서 layout_test.html을 열어 레이아웃을 확인하세요.")

if __name__ == "__main__":
    print("=" * 60)
    print("과일다리 레이아웃 수정 스크립트")
    print("=" * 60)
    print()

    # layout-fix.css 파일 확인
    layout_fix_file = BASE_DIR / "styles" / "layout-fix.css"
    if not layout_fix_file.exists():
        print("❌ layout-fix.css 파일이 없습니다!")
        print("   먼저 styles/layout-fix.css 파일을 생성하세요.")
        exit(1)

    print("✅ layout-fix.css 파일 확인됨")
    print()

    # 모든 HTML 파일에 적용
    updated = process_all_html_files()

    # 테스트 페이지 생성
    create_test_page()

    print("\n🎉 레이아웃 수정 작업 완료!")