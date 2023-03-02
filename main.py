"""
Este módulo crea un archivo HTML de ejemplo en la carpeta 'build'
"""

import os

if not os.path.exists('build'):
    os.makedirs('build')

with open('build/index.html', 'w', encoding='utf-8') as f:
    f.write('<html><body><h1>Testing pipeline</h1></body></html>')
