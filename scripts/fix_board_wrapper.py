import re

# Read the HTML file
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Slide 8 (line ~1430)
# Find the table in slide 8 and wrap it with board div
slide_8_pattern = r'(data-slide-index="8".*?<div class="pill">Launch Pair, Expansion, Bridge</div>\s*</div>\s*)(<table class="table" style="margin-top:16px">.*?</table>)(\s*</div>)'

def slide_8_replacement(match):
    return match.group(1) + '<div class="board">\n              ' + match.group(2) + '\n              </div>' + match.group(3)

content = re.sub(slide_8_pattern, slide_8_replacement, content, flags=re.DOTALL)

# Fix Slide 12 (line ~1671)
# Find the table in slide 12 and wrap it with board div
slide_12_pattern = r'(data-slide-index="12".*?핵심 전략은 슬로건이 아닙니다.*?</div>\s*</div>\s*)(<table class="table">.*?</table>)(\s*</div>)'

def slide_12_replacement(match):
    return match.group(1) + '<div class="board">\n              ' + match.group(2) + '\n              </div>' + match.group(3)

content = re.sub(slide_12_pattern, slide_12_replacement, content, flags=re.DOTALL)

# Write the fixed content
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed slide 8: Added board wrapper around table")
print("Fixed slide 12: Added board wrapper around table")
print("\nBoth slides now have consistent structure with other slides.")
