import re

# Read the original HTML file
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all slide content (data-slide-index sections)
slides_data = []
pattern = r'<section class="slide[^"]*"\s+data-slide-index="(\d+)"[^>]*>(.*?)</section>\s*</section>'

for match in re.finditer(pattern, content, re.DOTALL):
    index = match.group(1)
    slide_content = match.group(2)
    slides_data.append({
        'index': index,
        'content': slide_content
    })

print(f"Extracted {len(slides_data)} slides")

# Extract the head section (styles)
head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL)
head_content = head_match.group(1) if head_match else ''

# Extract topbar
topbar_match = re.search(r'(<header class="topbar">.*?</header>)', content, re.DOTALL)
topbar_content = topbar_match.group(1) if topbar_match else ''

print("Extracted head and topbar")
print(f"Topbar length: {len(topbar_content)}")
print("\nRebuilding HTML with new slide structure...")

# Build new HTML from scratch
new_html = f'''<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fruit Commerce Proposal</title>
  <style>
    :root {{
      --bg: #f5efe5;
      --paper: #fffaf3;
      --ink: #1f1a16;
      --muted: #675f56;
      --line: rgba(31, 26, 22, .10);
      --accent: #cb5b2c;
      --olive: #556548;
      --berry: #a14253;
      --gold: #a97828;
      --shadow: 0 24px 60px rgba(43, 31, 18, .10);
      --display: "Iowan Old Style", "Palatino Linotype", "Apple SD Gothic Neo", "Malgun Gothic", serif;
      --body: "Noto Sans KR", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html, body {{
      height: 100%;
      overflow: hidden;
    }}

    body {{
      font-family: var(--body);
      color: var(--ink);
      background: radial-gradient(circle at 0 0, rgba(203, 91, 44, .15), transparent 24%),
                  radial-gradient(circle at 100% 0, rgba(85, 101, 72, .14), transparent 22%),
                  linear-gradient(180deg, #f7f1e7 0, #f2ebdf 100%);
    }}

    /* Topbar styles */
    .topbar {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 100;
      background: rgba(247, 241, 231, .95);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid rgba(31, 26, 22, .08);
      padding: 14px 20px;
    }}

    .topbar-inner {{
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }}

    .brand {{
      font-size: 14px;
      font-weight: 900;
      letter-spacing: .12em;
      text-transform: uppercase;
    }}

    .brand span {{
      color: var(--accent);
    }}

    .slide-counter {{
      font-size: 12px;
      font-weight: 700;
      color: var(--muted);
    }}

    .slide-counter strong {{
      color: var(--ink);
    }}

    /* Slide container - new simple structure */
    .slides-container {{
      position: fixed;
      top: 60px;
      left: 0;
      right: 0;
      bottom: 0;
      overflow: hidden;
    }}

    .slide-wrapper {{
      width: 100%;
      height: 100%;
      position: relative;
    }}

    .slide {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.5s ease, visibility 0.5s;
      overflow-y: auto;
      padding: 40px 20px;
    }}

    .slide.active {{
      opacity: 1;
      visibility: visible;
      z-index: 1;
    }}

    .slide-content {{
      max-width: 1400px;
      margin: 0 auto;
      background: rgba(255, 250, 243, .90);
      border-radius: 24px;
      padding: 40px;
      box-shadow: 0 24px 60px rgba(43, 31, 18, .10);
      min-height: calc(100vh - 180px);
    }}

    /* Navigation */
    .nav-controls {{
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 200;
      display: flex;
      gap: 12px;
      background: rgba(255, 255, 255, .95);
      padding: 12px 20px;
      border-radius: 999px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, .15);
    }}

    .nav-btn {{
      padding: 10px 20px;
      border: none;
      border-radius: 999px;
      background: var(--accent);
      color: white;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .nav-btn:hover {{
      background: #b54a22;
      transform: scale(1.05);
    }}

    .nav-btn:disabled {{
      background: rgba(31, 26, 22, .2);
      cursor: not-allowed;
      transform: scale(1);
    }}

    .page-indicator {{
      display: flex;
      align-items: center;
      padding: 0 16px;
      font-size: 14px;
      font-weight: 700;
      color: var(--ink);
    }}

    /* Content styles - copy from original */
'''

# Extract all style rules from original
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if style_match:
    original_styles = style_match.group(1)
    # Extract content-specific styles (titles, tables, cards, etc.)
    # We'll keep styles for: title, kicker, desc, table, card, board, chart, grid, etc.
    content_styles = []

    # Find styles for content elements
    for selector in ['.kicker', '.title', '.desc', '.pill', '.section', '.section-shell',
                     '.section-head', '.board', '.chart', '.table', '.card', '.grid-2',
                     '.hero-grid', '.hero-shell', '.slide-meta', '.slide-tag', '.compare-table',
                     '.compare-row', '.compare-label', '.compare-box']:
        pattern_selector = re.escape(selector) + r'\s*\{[^}]+\}'
        matches = re.findall(pattern_selector, original_styles, re.DOTALL)
        content_styles.extend(matches)

    new_html += '\n    ' + '\n    '.join(content_styles)

new_html += '''
  </style>
</head>

<body>
  <!-- Topbar -->
  <header class="topbar">
    <div class="topbar-inner">
      <div class="brand">Fruit <span>Commerce</span></div>
      <div class="slide-counter">
        <span id="current-page">1</span> / <span id="total-pages">24</span>
      </div>
    </div>
  </header>

  <!-- Slides Container -->
  <div class="slides-container">
    <div class="slide-wrapper">
'''

# Add all slides
for i, slide in enumerate(slides_data):
    active_class = ' active' if i == 0 else ''
    new_html += f'''
      <div class="slide{active_class}" data-slide="{slide['index']}">
        <div class="slide-content">
          {slide['content']}
        </div>
      </div>
'''

new_html += '''
    </div>
  </div>

  <!-- Navigation Controls -->
  <div class="nav-controls">
    <button class="nav-btn" id="prev-btn">← Prev</button>
    <div class="page-indicator">
      <span id="page-num">1</span> / <span>24</span>
    </div>
    <button class="nav-btn" id="next-btn">Next →</button>
  </div>

  <script>
    // Simple slide navigation
    let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const pageNum = document.getElementById('page-num');
    const currentPage = document.getElementById('current-page');
    const totalPages = document.getElementById('total-pages');

    totalPages.textContent = totalSlides;

    function showSlide(index) {
      // Clamp index
      if (index < 0) index = 0;
      if (index >= totalSlides) index = totalSlides - 1;

      // Hide all slides
      slides.forEach(slide => {
        slide.classList.remove('active');
      });

      // Show current slide
      slides[index].classList.add('active');
      currentSlide = index;

      // Update UI
      pageNum.textContent = index + 1;
      currentPage.textContent = index + 1;

      // Update buttons
      prevBtn.disabled = (index === 0);
      nextBtn.disabled = (index === totalSlides - 1);

      // Scroll to top
      slides[index].scrollTop = 0;
    }

    // Event listeners
    prevBtn.addEventListener('click', () => showSlide(currentSlide - 1));
    nextBtn.addEventListener('click', () => showSlide(currentSlide + 1));

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft' || e.key === 'Left') {
        e.preventDefault();
        showSlide(currentSlide - 1);
      } else if (e.key === 'ArrowRight' || e.key === 'Right' || e.key === ' ') {
        e.preventDefault();
        showSlide(currentSlide + 1);
      } else if (e.key === 'Home') {
        e.preventDefault();
        showSlide(0);
      } else if (e.key === 'End') {
        e.preventDefault();
        showSlide(totalSlides - 1);
      }
    });

    // Initialize
    showSlide(0);
  </script>
</body>
</html>
'''

# Write new HTML
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"\n✓ Successfully rebuilt HTML with {len(slides_data)} slides")
print("✓ New slide system uses simple fade transitions")
print("✓ Fixed topbar, floating navigation controls")
print("✓ Keyboard navigation: Arrow keys, Space, Home, End")
