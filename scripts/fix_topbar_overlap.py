# -*- coding: utf-8 -*-
import re

input_file = r'C:\Users\dkskr\OneDrive\111\fruits\output\strategy_a_proposal_v2.html'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix deck-frame to add padding-top to prevent overlap with sticky topbar
# Topbar is approximately 60px tall
content = content.replace(
    '''    .deck-frame {
      position: relative;
      width: min(1480px, calc(100% - 12px));
      margin: 0 auto;
      padding: 10px 0 20px
    }''',
    '''    .deck-frame {
      position: relative;
      width: min(1480px, calc(100% - 12px));
      margin: 0 auto;
      padding: 70px 0 20px
    }'''
)

# Also adjust the :before and :after pseudo-elements top position
content = content.replace(
    '''    .deck-frame:before,
    .deck-frame:after {
      content: "";
      position: absolute;
      top: 10px;
      bottom: 20px;
      width: 56px;
      z-index: 5;
      pointer-events: none
    }''',
    '''    .deck-frame:before,
    .deck-frame:after {
      content: "";
      position: absolute;
      top: 70px;
      bottom: 20px;
      width: 56px;
      z-index: 5;
      pointer-events: none
    }'''
)

# Adjust slide-shell height to account for the new padding
content = content.replace(
    '''    .slide-shell {
      min-height: calc(100vh - 100px);
      max-height: calc(100vh - 100px);
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 8px;
      padding: 0;
      overflow: visible
    }''',
    '''    .slide-shell {
      min-height: calc(100vh - 160px);
      max-height: calc(100vh - 160px);
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 8px;
      padding: 0;
      overflow: visible
    }'''
)

with open(input_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed topbar overlap successfully!")
print("Changes:")
print("1. .deck-frame padding-top: 10px -> 70px (prevents overlap with sticky topbar)")
print("2. .deck-frame:before/after top: 10px -> 70px (adjust fade gradients)")
print("3. .slide-shell height: calc(100vh - 100px) -> calc(100vh - 160px)")
print("")
print("Now slide content will not go behind the sticky header!")
