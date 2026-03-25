#!/usr/bin/env python3
"""
모든 HTML 파일에 common-layout.css 적용
과일다리 프로젝트 - 공통 레이아웃 스타일 적용 스크립트
"""

import os
import re
from pathlib import Path

# 경로 설정
BASE_DIR = Path(".")
PAGES_DIR = BASE_DIR / "pages"

def add_common_layout_css(file_path):
    """HTML 파일에 common-layout.css 추가"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"[ERROR] Failed to read {file_path}: {e}")
        return False

    # 이미 common-layout.css가 포함되어 있는지 확인
    if 'common-layout.css' in content:
        return 'already'

    # components.css 다음에 common-layout.css 추가
    # 먼저 components.css 링크를 찾는다
    pattern = r'(<link rel="stylesheet" href="[^"]*components\.css">)'

    # common-layout.css 추가
    replacement = r'\1\n    <link rel="stylesheet" href="../../styles/common-layout.css">'

    new_content, count = re.subn(pattern, replacement, content)

    # 변경사항이 있으면 저장
    if count > 0:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return 'updated'
        except Exception as e:
            print(f"[ERROR] Failed to write {file_path}: {e}")
            return False
    else:
        # components.css가 없는 경우, design-system.css 다음에 추가
        pattern2 = r'(<link rel="stylesheet" href="[^"]*design-system\.css">)'
        replacement2 = r'\1\n    <link rel="stylesheet" href="../../styles/components.css">\n    <link rel="stylesheet" href="../../styles/common-layout.css">'

        new_content, count = re.subn(pattern2, replacement2, content)

        if count > 0:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return 'updated_with_components'
            except Exception as e:
                print(f"[ERROR] Failed to write {file_path}: {e}")
                return False

    return 'no_match'

def process_all_html_files():
    """모든 HTML 파일 처리"""
    stats = {
        'updated': 0,
        'updated_with_components': 0,
        'already': 0,
        'no_match': 0,
        'error': 0,
        'total': 0
    }

    print("=" * 60)
    print("FruitBridge Common Layout CSS Application")
    print("=" * 60)
    print()

    # pages 디렉토리의 모든 HTML 파일 찾기
    html_files = list(PAGES_DIR.rglob("*.html"))
    stats['total'] = len(html_files)

    print(f"Found {stats['total']} HTML files in pages directory\n")

    for html_file in html_files:
        result = add_common_layout_css(html_file)
        relative_path = html_file.relative_to(BASE_DIR)

        if result == 'updated':
            stats['updated'] += 1
            print(f"[OK] Updated: {relative_path}")
        elif result == 'updated_with_components':
            stats['updated_with_components'] += 1
            print(f"[OK] Updated (+ components.css): {relative_path}")
        elif result == 'already':
            stats['already'] += 1
            print(f"[--] Skipped: {relative_path} (already has common-layout.css)")
        elif result == 'no_match':
            stats['no_match'] += 1
            print(f"[??] No match: {relative_path} (couldn't find insertion point)")
        else:
            stats['error'] += 1
            print(f"[!!] Error: {relative_path}")

    # 결과 요약
    print("\n" + "=" * 60)
    print("Summary:")
    print("=" * 60)
    print(f"Total files:                 {stats['total']}")
    print(f"Updated:                     {stats['updated']}")
    print(f"Updated with components:     {stats['updated_with_components']}")
    print(f"Already had common-layout:   {stats['already']}")
    print(f"No match found:              {stats['no_match']}")
    print(f"Errors:                      {stats['error']}")
    print()

    success_count = stats['updated'] + stats['updated_with_components'] + stats['already']
    print(f"Success rate: {success_count}/{stats['total']} ({success_count*100/stats['total']:.1f}%)")

    if stats['no_match'] > 0:
        print("\nNote: Some files couldn't be updated. They might have different structure.")

    return stats

def check_specific_pages():
    """특정 중요 페이지들 확인"""
    important_pages = [
        "pages/products/best.html",
        "pages/products/category.html",
        "pages/products/all.html",
        "pages/home/fruit_commerce_fruitbridge.html",
        "pages/auth/login.html",
        "pages/mypage/index.html",
        "pages/cart/index.html"
    ]

    print("\n" + "=" * 60)
    print("Checking Important Pages:")
    print("=" * 60)

    for page_path in important_pages:
        file_path = BASE_DIR / page_path
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            has_design = 'design-system.css' in content
            has_components = 'components.css' in content
            has_common = 'common-layout.css' in content

            status = []
            if has_design:
                status.append("design-system")
            if has_components:
                status.append("components")
            if has_common:
                status.append("common-layout")

            status_str = ", ".join(status) if status else "NO CSS"
            print(f"{page_path:50} [{status_str}]")
        else:
            print(f"{page_path:50} [NOT FOUND]")

if __name__ == "__main__":
    print("Starting Common Layout CSS Application...")
    print()

    # common-layout.css 파일 확인
    common_layout_file = BASE_DIR / "styles" / "common-layout.css"
    if not common_layout_file.exists():
        print("[ERROR] common-layout.css file not found!")
        print("        Please ensure styles/common-layout.css exists.")
        exit(1)

    print("[OK] common-layout.css file found")
    print()

    # 모든 HTML 파일에 적용
    stats = process_all_html_files()

    # 중요 페이지 확인
    check_specific_pages()

    print("\n" + "=" * 60)
    print("Common Layout CSS application completed!")
    print("=" * 60)