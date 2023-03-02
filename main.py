"""
Este módulo crea un archivo HTML de ejemplo en la carpeta 'build'
"""
import os


def main():
    """
    Este método crea un archivo HTML de ejemplo en la carpeta 'build'
    """
    if not os.path.exists('build'):
        os.makedirs('build')

    with open('build/index.html', 'w', encoding='utf-8') as file:
        file.write('<html><body><h1>Testing pipeline</h1></body></html>')


if __name__ == '__main__':
    main()
