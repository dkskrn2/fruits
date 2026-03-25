#!/usr/bin/env python3
"""
FruitBridge CV3 디자인 시스템 완전 재구성 스크립트
모든 HTML 파일을 깨끗한 CV3 디자인 시스템으로 재구성
"""

import os
import re
from pathlib import Path

# 경로 설정
BASE_DIR = Path("C:/Users/dkskr/OneDrive/111/fruits/output")
PAGES_DIR = BASE_DIR / "pages"

# 새로운 CSS 링크
CV3_CSS_LINKS = """    <!-- FruitBridge CV3 Design System CSS -->
    <link rel="stylesheet" href="../../styles/fruitbridge-core.css">
    <link rel="stylesheet" href="../../styles/fruitbridge-base.css">
    <link rel="stylesheet" href="../../styles/fruitbridge-components.css">
    <link rel="stylesheet" href="../../styles/pages.css">"""

def rebuild_html_file(file_path):
    """HTML 파일을 CV3 디자인 시스템에 맞게 재구성"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. CSS 링크 업데이트 (모든 기존 링크 제거 후 CV3 링크 추가)
    # 기존 CSS 링크 모두 제거
    content = re.sub(
        r'<link[^>]*?rel="stylesheet"[^>]*?>\s*',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # title 태그 뒤에 CV3 CSS 링크 추가
    title_pattern = r'(</title>)\s*'
    replacement = r'\1\n' + CV3_CSS_LINKS + '\n'
    content = re.sub(title_pattern, replacement, content, count=1)

    # 2. 클래스명 정리 (중복/잘못된 클래스 제거)
    # btn btn-primary btn-full처럼 된 것들을 정리
    content = re.sub(r'class="([^"]+)"', lambda m: f'class="{clean_classes(m.group(1))}"', content)

    return content

def clean_classes(class_string):
    """클래스명 문자열 정리"""
    classes = class_string.split()
    unique_classes = []
    seen = set()

    for cls in classes:
        # CV3 클래스만 유지
        if cls not in seen:
            seen.add(cls)
            unique_classes.append(cls)

    return ' '.join(unique_classes)

def process_all_files():
    """모든 HTML 파일 처리"""
    processed = 0
    errors = []

    for html_file in PAGES_DIR.glob('**/*.html'):
        # 백업 파일과 CV3 샘플은 제외
        if '.backup' in str(html_file) or '_cv3.html' in str(html_file):
            continue

        try:
            # HTML 재구성
            rebuilt_content = rebuild_html_file(html_file)

            # 파일 저장
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(rebuilt_content)

            processed += 1
            print(f"[OK] Rebuilt: {html_file.relative_to(PAGES_DIR)}")

        except Exception as e:
            errors.append(f"[ERROR] {html_file}: {e}")

    return processed, errors

def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("FruitBridge CV3 Clean Rebuild")
    print("=" * 60)

    # HTML 파일 처리
    print("\nRebuilding HTML files with CV3 Design System...")
    count, errors = process_all_files()

    # 결과 출력
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"[OK] Files rebuilt: {count}")

    if errors:
        print(f"\n[WARNING] Errors: {len(errors)}")
        for error in errors[:5]:
            print(f"  {error}")

    print("\n[INFO] All HTML files now use clean CV3 Design System!")
    print("[INFO] CSS structure:")
    print("  - fruitbridge-core.css: Design tokens")
    print("  - fruitbridge-base.css: Reset & base styles")
    print("  - fruitbridge-components.css: Component styles")
    print("  - pages.css: Page-specific styles")

if __name__ == "__main__":
    main()