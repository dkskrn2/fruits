import re

# Read the original file with slide 1
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal.html', 'r', encoding='utf-8') as f:
    original = f.read()

# Read the current file (missing slide 1)
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'r', encoding='utf-8') as f:
    current = f.read()

# Extract slide 1 from original using line-based approach
original_lines = original.splitlines(keepends=True)

# Find slide 1 (lines 904-950)
slide_1_start = None
slide_1_end = None

for i, line in enumerate(original_lines):
    if 'data-slide-index="1"' in line:
        slide_1_start = i
    if slide_1_start is not None and i > slide_1_start:
        # Look for the closing </section> that ends the slide
        if '</section>' in line and 'data-slide-index="2"' in original_lines[min(i+1, len(original_lines)-1)]:
            slide_1_end = i + 1
            break

if slide_1_start is None or slide_1_end is None:
    print("ERROR: Could not find slide 1 boundaries in original file")
    print(f"Start: {slide_1_start}, End: {slide_1_end}")
    exit(1)

slide_1_content = ''.join(original_lines[slide_1_start:slide_1_end])
print(f"Extracted slide 1 from lines {slide_1_start+1} to {slide_1_end} ({len(slide_1_content)} characters)")

# Find the position to insert slide 1 (after slide 0, before slide 2)
# Use line-based approach for current file too
current_lines = current.splitlines(keepends=True)

slide_0_end_line = None
for i, line in enumerate(current_lines):
    if 'data-slide-index="0"' in line:
        # Find the end of this slide
        for j in range(i+1, len(current_lines)):
            if 'data-slide-index="2"' in current_lines[j]:
                slide_0_end_line = j
                break
        break

if slide_0_end_line is None:
    print("ERROR: Could not find slide 0 end in current file")
    exit(1)

print(f"Insert position found at line {slide_0_end_line}")

# Insert slide 1 before slide 2
new_lines = current_lines[:slide_0_end_line] + [slide_1_content] + current_lines[slide_0_end_line:]
new_content = ''.join(new_lines)

# Write the updated file
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SUCCESS: Slide 1 inserted")
print("Verifying...")

# Verify
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'r', encoding='utf-8') as f:
    verify = f.read()

slides_found = len(re.findall(r'data-slide-index="(\d+)"', verify))
print(f"Total slides now: {slides_found}")

# List all slide indices
indices = sorted([int(x) for x in re.findall(r'data-slide-index="(\d+)"', verify)])
print(f"Slide indices: {indices}")

if slides_found == 18 and indices == list(range(18)):
    print("SUCCESS: All 18 slides (0-17) are now present!")
else:
    print(f"WARNING: Expected 18 slides with indices 0-17, got {slides_found} slides")
