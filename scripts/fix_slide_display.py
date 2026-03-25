import re

with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Fixing slide display issues...")

# Count scripts
script_matches = list(re.finditer(r'<script>(.*?)</script>', content, re.DOTALL))
print(f"Found {len(script_matches)} script sections")

# Remove all existing scripts
content = re.sub(r'<script>.*?</script>', '', content, flags=re.DOTALL)
print("Removed old scripts")

# Add clean single script before </body>
new_script = '''  <script>
    // Wait for DOM to be ready
    document.addEventListener('DOMContentLoaded', function() {
      const slides = Array.from(document.querySelectorAll('.slide'));
      const totalSlides = slides.length;
      let currentSlide = 0;

      console.log('Slide system initializing...');
      console.log('Total slides found:', totalSlides);

      // Debug: List all slide indices
      slides.forEach((slide, i) => {
        const index = slide.getAttribute('data-slide-index');
        console.log('Slide', i, 'has index:', index);
      });

      const navButtons = document.querySelectorAll('.nav-btn[data-slide-target]');
      const state = document.getElementById('page-state');
      const bar = document.getElementById('progress-bar');
      const prev = document.getElementById('prev-page');
      const next = document.getElementById('next-page');

      function showSlide(index) {
        if (index < 0) index = 0;
        if (index >= totalSlides) index = totalSlides - 1;

        console.log('Switching to slide', index);

        // Hide all slides
        slides.forEach((slide, i) => {
          slide.classList.remove('active');
          slide.style.opacity = '0';
          slide.style.visibility = 'hidden';
          slide.style.display = 'none';
        });

        // Show target slide
        if (slides[index]) {
          slides[index].classList.add('active');
          slides[index].style.opacity = '1';
          slides[index].style.visibility = 'visible';
          slides[index].style.display = 'block';
          slides[index].scrollTop = 0;
        }

        currentSlide = index;
        updateUI(index);
      }

      function updateUI(index) {
        if (state) {
          state.textContent = (index + 1) + ' / ' + totalSlides;
        }

        if (bar) {
          const progress = ((index + 1) / totalSlides) * 100;
          bar.style.width = progress + '%';
        }

        navButtons.forEach(btn => {
          const target = Number(btn.dataset.slideTarget);
          btn.classList.toggle('active', target === index);
        });

        if (prev) prev.disabled = (index === 0);
        if (next) next.disabled = (index === totalSlides - 1);
      }

      // Navigation handlers
      navButtons.forEach(button => {
        button.addEventListener('click', () => {
          const target = Number(button.dataset.slideTarget);
          showSlide(target);
        });
      });

      if (prev) {
        prev.addEventListener('click', () => {
          console.log('Previous clicked');
          showSlide(currentSlide - 1);
        });
      }

      if (next) {
        next.addEventListener('click', () => {
          console.log('Next clicked');
          showSlide(currentSlide + 1);
        });
      }

      // Keyboard navigation
      window.addEventListener('keydown', (event) => {
        if (event.key === 'ArrowRight' || event.key === 'Right' || event.key === ' ') {
          event.preventDefault();
          console.log('Next key pressed');
          showSlide(currentSlide + 1);
        } else if (event.key === 'ArrowLeft' || event.key === 'Left') {
          event.preventDefault();
          console.log('Previous key pressed');
          showSlide(currentSlide - 1);
        } else if (event.key === 'Home') {
          event.preventDefault();
          showSlide(0);
        } else if (event.key === 'End') {
          event.preventDefault();
          showSlide(totalSlides - 1);
        }

        // Number keys 1-9 to jump to slides
        const num = parseInt(event.key);
        if (num >= 1 && num <= 9) {
          event.preventDefault();
          showSlide(num - 1);
        }
      });

      // Initialize
      showSlide(0);
      console.log('Slide system ready! Press arrow keys to navigate.');
      console.log('Total slides:', totalSlides, '(indices 0-' + (totalSlides-1) + ')');
    });
  </script>
</body>

</html>'''

# Replace end of file
content = re.sub(r'</body>\s*</html>\s*$', new_script, content, flags=re.DOTALL)

# Save
with open('C:/Users/dkskr/OneDrive/111/fruits/output/strategy_a_proposal_v2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nSUCCESS: Fixed slide display system")
print("- Removed duplicate scripts")
print("- Added explicit display block/none")
print("- Added DOMContentLoaded wrapper")
print("- Enhanced console logging for debugging")
print("- Added number key shortcuts (1-9)")
print("\nOpen the HTML file and press F12 to see console logs")
print("Use arrow keys or number keys to navigate slides")