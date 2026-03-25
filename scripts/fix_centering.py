# -*- coding: utf-8 -*-
import re

input_file = r'C:\Users\dkskr\OneDrive\111\fruits\output\strategy_a_proposal_v2.html'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix slide-shell
content = re.sub(
    r'\.slide-shell \{[^}]+\}',
    '''.slide-shell {
      min-height: calc(100vh - 100px);
      max-height: calc(100vh - 100px);
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 8px;
      padding: 0;
      overflow: visible
    }''',
    content,
    count=1
)

# Add height to hero-shell and section-shell
content = content.replace(
    '''    .hero-shell,
    .section-shell {
      background: rgba(255, 250, 243, .88);
      border: 1px solid rgba(31, 26, 22, .08);
      border-radius: 28px;
      box-shadow: var(--shadow);
      overflow: hidden
    }''',
    '''    .hero-shell,
    .section-shell {
      height: 100%;
      background: rgba(255, 250, 243, .88);
      border: 1px solid rgba(31, 26, 22, .08);
      border-radius: 28px;
      box-shadow: var(--shadow);
      overflow: hidden
    }'''
)

# Fix hero-grid
content = content.replace(
    '''    .hero-grid {
      display: grid;
      grid-template-columns: 1.2fr .8fr
    }''',
    '''    .hero-grid {
      display: grid;
      grid-template-columns: 1.2fr .8fr;
      height: 100%;
      align-items: stretch
    }'''
)

with open(input_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed successfully! Slides should now be centered and fill the screen.")
