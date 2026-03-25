# -*- coding: utf-8 -*-
import re

# Read the HTML file
input_file = r'C:\Users\dkskr\OneDrive\111\fruits\output\strategy_a_proposal_v2.html'
output_file = r'C:\Users\dkskr\OneDrive\111\fruits\output\strategy_a_proposal_v2.html'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the scroll event listener (remove width check)
old_scroll = '''      deck.addEventListener('scroll', () => {
        if (window.innerWidth <= 1100) return;
        const nextIndex = Math.round(deck.scrollLeft / deck.clientWidth);
        syncUI(nextIndex);
      }, { passive: true });'''

new_scroll = '''      deck.addEventListener('scroll', () => {
        const nextIndex = Math.round(deck.scrollLeft / deck.clientWidth);
        syncUI(nextIndex);
      }, { passive: true });'''

content = content.replace(old_scroll, new_scroll)

# Fix the keydown event listener (remove width check and add more keys)
old_keydown = '''      window.addEventListener('keydown', (event) => {
        if (window.innerWidth <= 1100) return;
        if (event.key === 'ArrowRight') goToSlide(currentIndex + 1);
        if (event.key === 'ArrowLeft') goToSlide(currentIndex - 1);
      });'''

new_keydown = '''      window.addEventListener('keydown', (event) => {
        if (event.key === 'ArrowRight' || event.key === 'Right') {
          event.preventDefault();
          goToSlide(currentIndex + 1);
        }
        if (event.key === 'ArrowLeft' || event.key === 'Left') {
          event.preventDefault();
          goToSlide(currentIndex - 1);
        }
        if (event.key === ' ' || event.key === 'Spacebar') {
          event.preventDefault();
          goToSlide(currentIndex + 1);
        }
      });'''

content = content.replace(old_keydown, new_keydown)

# Write back to file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Navigation fixed successfully!")
print("Changes:")
print("1. Removed window width restriction for scroll and keyboard navigation")
print("2. Added preventDefault() to prevent default browser behavior")
print("3. Added spacebar support for next slide")
print("4. Navigation now works on all screen sizes")
