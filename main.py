import os

if not os.path.exists('build'):
    os.makedirs('build')

with open('build/index.html', 'w') as f:
    f.write('<html><body><h1>Testing pipeline</h1></body></html>')
