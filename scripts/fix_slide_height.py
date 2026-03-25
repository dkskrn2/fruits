# -*- coding: utf-8 -*-
import re

# Read the HTML file
input_file = r'C:\Users\dkskr\OneDrive\111\fruits\output\strategy_a_proposal_v2.html'
output_file = r'C:\Users\dkskr\OneDrive\111\fruits\output\strategy_a_proposal_v2.html'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the slide-shell height - increase from 106px to make it fill more of the screen
# The topbar is about 60px, so we need more space
old_slide_shell = '''    .slide-shell {
      height: calc(100vh - 106px);
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 8px;
      padding: 4px 0;
      overflow: hidden
    }'''

new_slide_shell = '''    .slide-shell {
      height: calc(100vh - 80px);
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 8px;
      padding: 20px 0;
      overflow-y: auto;
      overflow-x: hidden
    }'''

content = content.replace(old_slide_shell, new_slide_shell)

# Write back to file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Slide height fixed successfully!")
print("Changes:")
print("1. Height: calc(100vh - 106px) -> calc(100vh - 80px)")
print("2. Justify-content: center -> flex-start (top aligned)")
print("3. Padding: 4px 0 -> 20px 0 (more breathing room)")
print("4. Overflow: hidden -> overflow-y: auto (allow vertical scroll if needed)")
print("")
print("Now slides should:")
print("- Fill more of the screen")
print("- Start from top instead of floating in middle")
print("- Allow scrolling for long content")
