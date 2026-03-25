# -*- coding: utf-8 -*-
import re

# Read the HTML file
input_file = r'C:\Users\dkskr\OneDrive\111\fruits\output\strategy_a_proposal_v2.html'
output_file = r'C:\Users\dkskr\OneDrive\111\fruits\output\strategy_a_proposal_v2.html'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the first occurrence of slide 13 (which should be 12) - line 1652
# This is the "Segment Offer Map" slide
first_slide_13 = '''      <section class="slide tone-4" data-slide-index="13" data-chapter="3">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">차별화</span>
            <strong>15 / 29</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Segment Offer Map</div>'''

fixed_first_slide_13 = '''      <section class="slide tone-4" data-slide-index="12" data-chapter="3">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">차별화</span>
            <strong>13 / 24</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Segment Offer Map</div>'''

# Replace the first slide 13 with slide 12
content = content.replace(first_slide_13, fixed_first_slide_13)

# Now fix the second slide 13 (which should stay as 13) - line 1707
# This is the "Secondary Route" slide - update the counter
second_slide_13 = '''      <section class="slide tone-4" data-slide-index="13" data-chapter="3">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">차별화</span>
            <strong>17 / 29</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Secondary Route</div>'''

fixed_second_slide_13 = '''      <section class="slide tone-4" data-slide-index="13" data-chapter="3">
        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">차별화</span>
            <strong>14 / 24</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Secondary Route</div>'''

content = content.replace(second_slide_13, fixed_second_slide_13)

# Also update slide 11 counter
slide_11_old = '''        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">차별화</span>
            <strong>15 / 29</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Competitive Positioning</div>'''

slide_11_new = '''        <div class="slide-shell">
          <div class="slide-meta">
            <span class="slide-tag">차별화</span>
            <strong>12 / 24</strong>
          </div>
          <section class="section">
            <div class="section-shell">
              <div class="section-head">
                <div>
                  <div class="kicker">Competitive Positioning</div>'''

content = content.replace(slide_11_old, slide_11_new, 1)

# Write back to file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Slide index fixed successfully!")
print("Changes:")
print("1. Slide 11 (Competitive Positioning): counter 15/29 -> 12/24")
print("2. First slide 13 (Segment Offer Map): index 13 -> 12, counter 15/29 -> 13/24")
print("3. Second slide 13 (Secondary Route): kept as 13, counter 17/29 -> 14/24")
print("4. Now sequence is correct: 11 -> 12 -> 13 -> 14 ...")
