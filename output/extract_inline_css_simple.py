#!/usr/bin/env python3
"""
FruitBridge CSS 분리 스크립트 (Simple Version)
- HTML 파일에서 인라인 <style> 태그 추출
- 카테고리별 CSS 파일 생성
- HTML 파일의 CSS 링크 업데이트
"""

import os
import re
from pathlib import Path

# 경로 설정
BASE_DIR = Path("C:/Users/dkskr/OneDrive/111/fruits/output")
PAGES_DIR = BASE_DIR / "pages"
STYLES_DIR = BASE_DIR / "styles"

# 새로운 CSS 파일 링크 (CV3 Design System)
CSS_LINKS_TEMPLATE = """    <!-- FruitBridge CV3 Design System CSS -->
    <link rel="stylesheet" href="../../styles/fruitbridge-core.css">
    <link rel="stylesheet" href="../../styles/fruitbridge-base.css">
    <link rel="stylesheet" href="../../styles/fruitbridge-components.css">
    <link rel="stylesheet" href="../../styles/{category_css}">"""

# 카테고리별 CSS 파일 매핑
CATEGORY_CSS_MAP = {
    'auth': 'auth.css',
    'cart': 'cart.css',
    'event': 'event.css',
    'home': 'home.css',
    'mypage': 'mypage.css',
    'order': 'order.css',
    'products': 'products.css',
    'search': 'search.css',
    'sitemap': 'sitemap.css',
    'support': 'support.css',
    'etc': 'misc.css'
}

def extract_inline_styles(html_content):
    """HTML에서 인라인 스타일 추출"""
    styles = []

    # <style> 태그 찾기 (multiline 포함)
    style_pattern = r'<style[^>]*?>(.*?)</style>'
    matches = re.findall(style_pattern, html_content, re.DOTALL | re.IGNORECASE)

    for match in matches:
        styles.append(match.strip())

    return '\n\n'.join(styles) if styles else None

def update_html_file(file_path, category):
    """HTML 파일 업데이트: 인라인 스타일 제거 및 CSS 링크 추가"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 백업 (원본 보존)
    original_content = content

    # 기존 CSS 링크 제거 (design-system.css, components.css)
    content = re.sub(
        r'<link[^>]*?href="[^"]*(?:design-system\.css|components\.css)"[^>]*?>\n?',
        '',
        content,
        flags=re.IGNORECASE
    )

    # <style> 태그 제거
    content = re.sub(
        r'<style[^>]*?>.*?</style>\s*',
        '',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    # </title> 태그 뒤에 새 CSS 링크 추가
    if category in CATEGORY_CSS_MAP:
        new_css = CSS_LINKS_TEMPLATE.format(category_css=CATEGORY_CSS_MAP[category])
    else:
        new_css = CSS_LINKS_TEMPLATE.format(category_css='misc.css')

    # </title> 태그 찾아서 그 뒤에 삽입
    title_pattern = r'(</title>\s*)'
    replacement = r'\1\n' + new_css + '\n'
    content = re.sub(title_pattern, replacement, content, count=1, flags=re.IGNORECASE)

    return content

def create_category_css_files():
    """카테고리별 CSS 파일 생성"""
    category_styles = {}

    # 각 카테고리 폴더 순회
    for category_dir in PAGES_DIR.iterdir():
        if category_dir.is_dir():
            category = category_dir.name
            if category not in category_styles:
                category_styles[category] = []

            # HTML 파일에서 스타일 추출
            for html_file in category_dir.glob('**/*.html'):
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                styles = extract_inline_styles(content)
                if styles:
                    # 파일별 주석 추가
                    relative_path = html_file.relative_to(PAGES_DIR)
                    comment = f"/* ========== Styles from {relative_path} ========== */"
                    category_styles[category].append(comment)
                    category_styles[category].append(styles)

    # CSS 파일 생성
    created_files = []
    for category, styles_list in category_styles.items():
        if styles_list and category in CATEGORY_CSS_MAP:
            css_file = STYLES_DIR / CATEGORY_CSS_MAP[category]

            # 헤더 추가
            header = f"""/* ================================
   FruitBridge CV3 - {category.title()} Pages
   {category} 카테고리 페이지 전용 스타일
   ================================ */

"""

            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(header)
                f.write('\n\n'.join(styles_list))

            created_files.append(css_file.name)
            print(f"[OK] Created: {css_file.name}")

    return created_files

def process_all_html_files():
    """모든 HTML 파일 처리"""
    processed = 0
    errors = []

    for category_dir in PAGES_DIR.iterdir():
        if category_dir.is_dir():
            category = category_dir.name

            for html_file in category_dir.glob('**/*.html'):
                # 백업 파일은 제외
                if '.backup' in str(html_file):
                    continue

                try:
                    # HTML 파일 업데이트
                    updated_content = update_html_file(html_file, category)

                    # 파일 저장
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(updated_content)

                    processed += 1
                    relative_path = html_file.relative_to(PAGES_DIR)
                    print(f"[OK] Updated: {relative_path}")

                except Exception as e:
                    errors.append(f"[ERROR] Error processing {html_file}: {e}")

    return processed, errors

def test_single_file():
    """단일 파일 테스트"""
    test_file = PAGES_DIR / "auth" / "login.html"

    print("\n[TEST] Test file: login.html")
    print("-" * 60)

    # 원본 읽기
    with open(test_file, 'r', encoding='utf-8') as f:
        original = f.read()

    # 스타일 추출
    styles = extract_inline_styles(original)
    if styles:
        print(f"[OK] Extracted styles length: {len(styles)} characters")

    # HTML 업데이트
    updated = update_html_file(test_file, 'auth')
    print(f"[OK] Updated HTML length: {len(updated)} characters (original: {len(original)})")

    # CSS 링크 확인
    if 'fruitbridge-core.css' in updated and 'auth.css' in updated:
        print("[OK] CSS links added correctly")

    # <style> 태그 제거 확인
    if '<style' not in updated.lower():
        print("[OK] Inline styles removed")

    print("-" * 60)

    response = input("\n계속 진행하시겠습니까? (y/n): ")
    return response.lower() == 'y'

def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("FruitBridge CSS 분리 작업")
    print("=" * 60)

    # 테스트 모드
    if not test_single_file():
        print("작업이 취소되었습니다.")
        return

    # 1. 카테고리별 CSS 파일 생성
    print("\n1. 카테고리별 CSS 파일 생성 중...")
    css_files = create_category_css_files()
    print(f"   -> {len(css_files)}개 CSS 파일 생성 완료")

    # 2. HTML 파일 업데이트
    print("\n2. HTML 파일 업데이트 중...")
    processed, errors = process_all_html_files()
    print(f"   -> {processed}개 HTML 파일 처리 완료")

    # 3. 결과 요약
    print("\n" + "=" * 60)
    print("작업 완료 요약")
    print("=" * 60)
    print(f"[OK] 생성된 CSS 파일: {len(css_files)}개")
    print(f"[OK] 업데이트된 HTML 파일: {processed}개")

    if errors:
        print(f"\n[WARNING]  오류 발생: {len(errors)}건")
        for error in errors[:5]:  # 처음 5개만 표시
            print(f"  {error}")

    print("\n💡 다음 CSS 파일들이 모든 페이지에 적용됩니다:")
    print("   - fruitbridge-core.css (디자인 토큰)")
    print("   - fruitbridge-base.css (리셋 & 기본 스타일)")
    print("   - fruitbridge-components.css (컴포넌트)")
    print("   - [category].css (카테고리별 전용 스타일)")

if __name__ == "__main__":
    main()