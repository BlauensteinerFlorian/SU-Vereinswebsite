content = open('src/index.html', 'r').read()

# Fix the sponsors section - wrap each image in a div
content = content.replace(
    '<div class="sponsors-grid">\n      \n      <a href="https://example.com" target="_blank" rel="noopener" class="sponsor-logo">\n        <div class="sponsor-item"><img src="/assets/sponsors/sponsor1.png" alt="Beispiel Sponsor 1" loading="lazy">\n      </a>',
    '<div class="sponsors-grid">\n      \n      <div class="sponsor-item">\n        <a href="https://example.com" target="_blank" rel="noopener">\n          <img src="/assets/sponsors/sponsor1.png" alt="Beispiel Sponsor 1" loading="lazy">\n        </a>\n      </div>'
)

content = content.replace(
    '<img src="/assets/sponsors/sponsor2.jpeg" alt="Beispiel Sponsor 2" loading="lazy">\n      </a>',
    '<img src="/assets/sponsors/sponsor2.jpeg" alt="Beispiel Sponsor 2" loading="lazy">\n      </div>'
)

content = content.replace(
    '</div>\n    </div>',
    '</div>'
)

open('src/index.html', 'w').write(content)
print("Fixed!")
