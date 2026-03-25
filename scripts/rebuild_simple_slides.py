import re

# Read the HTML file
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Processing HTML file...")

# Step 1: Replace horizontal scroll deck with simple stacked slides
# Find and replace the .deck CSS
content = re.sub(
    r'\.deck \{[^}]+\}',
    '''.deck {
      position: relative;
      width: 100%;
      height: calc(100vh - 60px);
      overflow: hidden;
    }''',
    content
)

# Step 2: Change slide CSS to use absolute positioning with opacity
content = re.sub(
    r'\.slide \{[^}]+\}',
    '''.slide {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.4s ease, visibility 0.4s;
      overflow-y: auto;
      scroll-snap-type: none;
    }''',
    content
)

# Add active slide class
active_slide_css = '''
    .slide.active {
      opacity: 1;
      visibility: visible;
      z-index: 1;
    }
'''

# Insert before </style>
content = content.replace('</style>', active_slide_css + '  </style>')

# Step 3: Remove scroll-snap from deck-frame
content = re.sub(
    r'scroll-snap-type:\s*x\s+mandatory;',
    '',
    content
)

# Step 4: Update JavaScript to use simple show/hide instead of scroll
old_js_pattern = r'<script>.*?</script>'
new_js = '''<script>
    // Simple slide navigation system
    const slides = Array.from(document.querySelectorAll('.slide'));
    const totalSlides = slides.length;
    let currentSlide = 0;

    const navButtons = document.querySelectorAll('.nav-btn[data-slide-target]');
    const state = document.getElementById('page-state');
    const bar = document.getElementById('progress-bar');
    const prev = document.getElementById('prev-page');
    const next = document.getElementById('next-page');
    const deck = document.querySelector('.deck');

    function showSlide(index) {
      // Clamp index
      if (index < 0) index = 0;
      if (index >= totalSlides) index = totalSlides - 1;

      // Hide all slides
      slides.forEach(slide => slide.classList.remove('active'));

      // Show target slide
      slides[index].classList.add('active');

      // Scroll to top of slide
      slides[index].scrollTop = 0;

      currentSlide = index;
      updateUI(index);
    }

    function updateUI(index) {
      // Update state indicator
      if (state) {
        state.textContent = `${index + 1} / ${totalSlides}`;
      }

      // Update progress bar
      if (bar) {
        const progress = ((index + 1) / totalSlides) * 100;
        bar.style.width = progress + '%';
      }

      // Update navigation buttons
      navButtons.forEach(btn => {
        const target = Number(btn.dataset.slideTarget);
        btn.classList.toggle('active', target === index);
      });

      // Update prev/next buttons
      if (prev) prev.disabled = (index === 0);
      if (next) next.disabled = (index === totalSlides - 1);
    }

    // Navigation button click handlers
    navButtons.forEach(button => {
      button.addEventListener('click', () => {
        const target = Number(button.dataset.slideTarget);
        showSlide(target);
      });
    });

    // Prev/Next buttons
    if (prev) prev.addEventListener('click', () => showSlide(currentSlide - 1));
    if (next) next.addEventListener('click', () => showSlide(currentSlide + 1));

    // Keyboard navigation
    window.addEventListener('keydown', (event) => {
      if (event.key === 'ArrowRight' || event.key === 'Right') {
        event.preventDefault();
        showSlide(currentSlide + 1);
      } else if (event.key === 'ArrowLeft' || event.key === 'Left') {
        event.preventDefault();
        showSlide(currentSlide - 1);
      } else if (event.key === ' ' || event.key === 'Spacebar') {
        event.preventDefault();
        showSlide(currentSlide + 1);
      } else if (event.key === 'Home') {
        event.preventDefault();
        showSlide(0);
      } else if (event.key === 'End') {
        event.preventDefault();
        showSlide(totalSlides - 1);
      }
    });

    // Initialize - show first slide
    showSlide(0);

    console.log(`Slide system initialized: ${totalSlides} slides`);
  </script>'''

content = re.sub(old_js_pattern, new_js, content, flags=re.DOTALL)

# Step 5: Add 'active' class to first slide
content = re.sub(
    r'(<section class="slide[^"]*" data-slide-index="0")',
    r'\1 active',
    content,
    count=1
)

# Write the modified content
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Rebuilt slide system")
print(f"- Changed from horizontal scroll to fade transitions")
print(f"- Slides now use absolute positioning with opacity")
print(f"- Removed scroll-snap behavior")
print(f"- Updated JavaScript for simple show/hide")
print(f"- Keyboard navigation: Arrow keys, Space, Home, End")
