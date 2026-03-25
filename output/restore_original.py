#!/usr/bin/env python3
"""
원본 HTML 파일 복원 스크립트
백업 파일(login.html.backup)의 구조를 기준으로 모든 HTML 파일 복원
"""

import os
import re
from pathlib import Path

# 경로 설정
BASE_DIR = Path("C:/Users/dkskr/OneDrive/111/fruits/output")
PAGES_DIR = BASE_DIR / "pages"
STYLES_DIR = BASE_DIR / "styles"

# 원본 CSS 링크 (백업 파일 기준)
ORIGINAL_CSS_LINKS = """    <link rel="stylesheet" href="../../styles/design-system.css">
    <link rel="stylesheet" href="../../styles/components.css">"""

def restore_html_files():
    """모든 HTML 파일을 원본 CSS 링크로 복원"""
    processed = 0

    for html_file in PAGES_DIR.glob('**/*.html'):
        # 백업 파일과 CV3 샘플은 제외
        if '.backup' in str(html_file) or '_cv3.html' in str(html_file):
            continue

        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # 현재 CV3 CSS 링크들을 제거
            content = re.sub(
                r'    <!-- FruitBridge CV3 Design System CSS -->.*?    <link rel="stylesheet" href="../../styles/pages\.css">',
                ORIGINAL_CSS_LINKS,
                content,
                flags=re.DOTALL
            )

            # 중복된 주석과 링크 제거
            content = re.sub(
                r'<!-- FruitBridge CV3 Design System CSS -->\s*',
                '',
                content
            )

            # 남은 Design System CSS 주석 정리
            content = re.sub(
                r'    <!-- Design System CSS -->\s*',
                '',
                content
            )

            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)

            processed += 1
            print(f"[OK] Restored: {html_file.relative_to(PAGES_DIR)}")

        except Exception as e:
            print(f"[ERROR] {html_file}: {e}")

    return processed

def main():
    print("=" * 60)
    print("Restoring Original HTML Files")
    print("=" * 60)

    # HTML 파일 복원
    count = restore_html_files()

    print(f"\n[OK] Restored {count} HTML files")
    print("\nNow all HTML files use original CSS links:")
    print("  - design-system.css")
    print("  - components.css")

if __name__ == "__main__":
    main()