content = open('src/index.html', 'r').read()

# Simple replacement
content = content.replace(
    'class="sponsor-logo"></a>',
    '''class="sponsor-logo">
          <img src="/assets/sponsors/sponsor1.png" alt="Beispiel Sponsor 1" loading="lazy">
        </a>
      </div>
      <div class="sponsor-item">
        <a href="https://example.com" target="_blank" rel="noopener" class="sponsor-logo">
          <img src="/assets/sponsors/sponsor2.jpeg" alt="Beispiel Sponsor 2" loading="lazy">'''
)

open('src/index.html', 'w').write(content)
print("Fixed!")
