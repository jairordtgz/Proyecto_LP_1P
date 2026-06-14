import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from lexer import analizar

DESARROLLADORES = {
    'Carlos':   ('CarlosLopez',    'algoritmo_carlos.dart'),
    'Jairo':    ('JairoRodriguez', 'algoritmo_jairo.dart'),
    'Benjamin': ('BenjaminCedeno', 'algoritmo_benjamin.dart'),
}

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in DESARROLLADORES:
        print('Uso: python run_lexer.py [Carlos | Jairo | Benjamin]')
        sys.exit(1)

    clave = sys.argv[1]
    desarrollador, archivo = DESARROLLADORES[clave]

    ruta = os.path.join(
        os.path.dirname(__file__), '..', 'algoritmos', archivo
    )

    if not os.path.exists(ruta):
        print(f'[Error] No se encontró: {ruta}')
        sys.exit(1)

    with open(ruta, 'r', encoding='utf-8') as f:
        codigo = f.read()

    print('=' * 64)
    print(f'  Archivo : {archivo}')
    print(f'  Autor   : {desarrollador}')
    print('=' * 64)
    analizar(codigo, desarrollador, archivo)

if __name__ == '__main__':
    main()