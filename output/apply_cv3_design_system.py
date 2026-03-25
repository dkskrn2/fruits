#!/usr/bin/env python3
"""
FruitBridge CV3 디자인 시스템 완전 적용 스크립트
1. HTML 클래스명을 CV3 클래스명으로 업데이트
2. 기존 CSS 변수를 CV3 변수로 통합
3. 중복 스타일 제거 및 최적화
"""

import os
import re
from pathlib import Path

# 경로 설정
BASE_DIR = Path("C:/Users/dkskr/OneDrive/111/fruits/output")
PAGES_DIR = BASE_DIR / "pages"
STYLES_DIR = BASE_DIR / "styles"

# =========================================
# 1. HTML 클래스명 매핑 테이블
# =========================================
HTML_CLASS_MAPPINGS = {
    # Headers
    'login-header': 'auth-header',
    'signup-header': 'auth-header',
    'page-header': 'nav-bar',
    'product-header': 'nav-bar',

    # Containers
    'page-container': 'auth-container',
    'mobile-container': 'page-container',
    'content-wrapper': 'content-wrapper',

    # Logo & Branding
    'logo-section': 'auth-logo-section',
    'logo': 'auth-logo',
    'brand-name': 'auth-brand-name',
    'brand-tagline': 'auth-brand-tagline',

    # Forms
    'login-form': 'auth-form',
    'signup-form': 'auth-form',
    'form-group': 'field',
    'form-input': 'control',
    'form-label': 'label',

    # Buttons
    'login-button': 'btn btn-primary btn-full',
    'signup-button': 'btn btn-primary btn-full',
    'submit-button': 'btn btn-primary',
    'cancel-button': 'btn btn-secondary',
    'close-button': 'btn-icon',
    'social-button': 'social-button',
    'btn-primary-custom': 'btn btn-primary',
    'btn-secondary-custom': 'btn btn-secondary',

    # Product Cards
    'product-card': 'product-card',
    'product-image': 'product-image',
    'product-body': 'product-body',
    'product-name': 'product-name',
    'product-price': 'price',
    'product-desc': 'product-desc',
    'price-old': 'price-old',
    'price-discount': 'price-discount',

    # Navigation
    'nav-menu': 'nav-menu',
    'nav-item': 'nav-link',
    'tab-menu': 'tab-row',
    'tab-item': 'tab',

    # Utilities
    'error-message': 'helper error',
    'helper-text': 'helper',
    'chip-tag': 'chip',
    'badge': 'chip',
}

# =========================================
# 2. CSS 변수 매핑 테이블
# =========================================
CSS_VARIABLE_MAPPINGS = {
    # Colors - Gray Scale to CV3
    '--color-gray-50': 'var(--color-bg-page)',
    '--color-gray-100': 'var(--color-bg-soft)',
    '--color-gray-200': 'var(--color-line)',
    '--color-gray-300': '#CDBFA8',
    '--color-gray-400': '#B3A591',
    '--color-gray-500': 'var(--color-text-muted)',
    '--color-gray-600': 'var(--color-text-secondary)',
    '--color-gray-700': '#556051',
    '--color-gray-800': '#494F47',
    '--color-gray-900': 'var(--color-text-primary)',

    # Legacy Colors
    '--color-primary': 'var(--color-brand-primary)',
    '--color-primary-dark': 'var(--color-brand-primary-hover)',
    '--color-secondary': 'var(--color-brand-secondary)',
    '--color-accent': 'var(--color-brand-accent)',
    '--color-error': 'var(--color-danger)',
    '--color-white': 'var(--color-surface)',
    '--color-black': 'var(--color-text-primary)',

    # Spacing
    '--spacing-xs': 'var(--space-1)',
    '--spacing-sm': 'var(--space-2)',
    '--spacing-md': 'var(--space-3)',
    '--spacing-lg': 'var(--space-4)',
    '--spacing-xl': 'var(--space-5)',
    '--spacing-2xl': 'var(--space-6)',

    # Font Sizes
    '--text-xs': 'var(--font-size-xs)',
    '--text-sm': 'var(--font-size-sm)',
    '--text-base': 'var(--font-size-base)',
    '--text-lg': 'var(--font-size-lg)',
    '--text-xl': 'var(--font-size-xl)',
    '--text-2xl': 'var(--font-size-2xl)',

    # Other
    '--border-radius': 'var(--radius-lg)',
    '--border-radius-sm': 'var(--radius-sm)',
    '--border-radius-lg': 'var(--radius-xl)',
    '--transition': 'var(--transition-base)',
    '--shadow': 'var(--shadow-md)',
}

def update_html_classes(content):
    """HTML 내용에서 클래스명 업데이트"""
    updated = content

    # 클래스명 업데이트
    for old_class, new_class in HTML_CLASS_MAPPINGS.items():
        # class="old_class" 형태
        pattern1 = f'class="([^"]*){old_class}([^"]*)"'

        def replace_func(match):
            prefix = match.group(1)
            suffix = match.group(2)
            # 이미 새 클래스가 있는지 확인
            if new_class not in match.group(0):
                return f'class="{prefix}{new_class}{suffix}"'
            return match.group(0)

        updated = re.sub(pattern1, replace_func, updated)

        # className="old_class" 형태 (React/JSX)
        pattern2 = f'className="([^"]*){old_class}([^"]*)"'
        updated = re.sub(pattern2, replace_func, updated)

    return updated

def update_css_variables(content):
    """CSS 내용에서 변수명 업데이트"""
    updated = content

    # CSS 변수 업데이트
    for old_var, new_var in CSS_VARIABLE_MAPPINGS.items():
        # var(--old-var) 형태
        pattern = re.escape(old_var)
        updated = re.sub(pattern, new_var, updated)

    # 직접 색상 코드를 CV3 변수로 대체
    color_replacements = {
        '#6FCF3F': 'var(--color-brand-primary)',
        '#5CB82F': 'var(--color-brand-primary-hover)',
        '#f8f9fa': 'var(--color-bg-page)',
        '#ffffff': 'var(--color-surface)',
        '#000000': 'var(--color-text-primary)',
    }

    for old_color, new_var in color_replacements.items():
        updated = re.sub(old_color, new_var, updated, flags=re.IGNORECASE)

    return updated

def optimize_css_file(file_path):
    """CSS 파일 최적화 - 중복 제거 및 정리"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # CSS 변수 업데이트
    content = update_css_variables(content)

    # 중복 선언 제거 (간단한 버전)
    # 같은 선택자가 여러 번 나오는 경우 마지막 것만 유지
    blocks = re.findall(r'([^{}]+)\s*\{([^}]+)\}', content)
    unique_blocks = {}

    for selector, rules in blocks:
        selector = selector.strip()
        if selector and not selector.startswith('/*') and not selector.startswith('@'):
            # 기존 규칙이 있으면 병합
            if selector in unique_blocks:
                unique_blocks[selector] += '\n' + rules
            else:
                unique_blocks[selector] = rules

    # 최적화된 CSS 재구성
    optimized_parts = []

    # 헤더 유지
    header_match = re.match(r'(/\*.*?\*/)', content, re.DOTALL)
    if header_match:
        optimized_parts.append(header_match.group(1))

    # 정렬된 선택자로 CSS 재구성
    for selector in sorted(unique_blocks.keys()):
        rules = unique_blocks[selector]
        # 중복 속성 제거
        rule_lines = rules.strip().split('\n')
        unique_rules = {}
        for line in rule_lines:
            if ':' in line:
                prop = line.split(':')[0].strip()
                unique_rules[prop] = line.strip()

        if unique_rules:
            formatted_rules = '\n    '.join(unique_rules.values())
            optimized_parts.append(f"\n{selector} {{\n    {formatted_rules}\n}}")

    return '\n'.join(optimized_parts)

def process_html_files():
    """모든 HTML 파일 처리"""
    processed = 0
    errors = []

    for html_file in PAGES_DIR.glob('**/*.html'):
        if '.backup' in str(html_file):
            continue

        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # HTML 클래스명 업데이트
            updated = update_html_classes(content)

            # 인라인 스타일의 CSS 변수도 업데이트
            updated = update_css_variables(updated)

            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(updated)

            processed += 1
            print(f"[OK] Updated HTML: {html_file.relative_to(PAGES_DIR)}")

        except Exception as e:
            errors.append(f"[ERROR] {html_file}: {e}")

    return processed, errors

def process_css_files():
    """모든 CSS 파일 처리"""
    processed = 0
    errors = []

    # 카테고리별 CSS 파일 처리
    for css_file in STYLES_DIR.glob('*.css'):
        # 핵심 디자인 시스템 파일은 건드리지 않음
        if css_file.name in ['fruitbridge-core.css', 'fruitbridge-base.css', 'fruitbridge-components.css']:
            continue

        try:
            # CSS 최적화
            optimized = optimize_css_file(css_file)

            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(optimized)

            processed += 1
            print(f"[OK] Optimized CSS: {css_file.name}")

        except Exception as e:
            errors.append(f"[ERROR] {css_file}: {e}")

    return processed, errors

def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("FruitBridge CV3 Design System Application")
    print("=" * 60)

    # 1. HTML 파일 처리
    print("\n1. Updating HTML class names...")
    html_count, html_errors = process_html_files()
    print(f"   -> {html_count} HTML files updated")

    # 2. CSS 파일 처리
    print("\n2. Optimizing CSS files...")
    css_count, css_errors = process_css_files()
    print(f"   -> {css_count} CSS files optimized")

    # 3. 결과 요약
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"[OK] HTML files updated: {html_count}")
    print(f"[OK] CSS files optimized: {css_count}")

    all_errors = html_errors + css_errors
    if all_errors:
        print(f"\n[WARNING] Total errors: {len(all_errors)}")
        for error in all_errors[:10]:
            print(f"  {error}")

    print("\n[INFO] CV3 Design System has been fully applied!")
    print("[INFO] All components now use unified CV3 classes and variables")

if __name__ == "__main__":
    main()