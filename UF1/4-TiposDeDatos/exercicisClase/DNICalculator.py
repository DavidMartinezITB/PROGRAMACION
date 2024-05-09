"""
David Martinez - ASIXc1A
M03 - UF1
Calculadora DNI
"""

LETRAS = (
    'T', 'R', 'W', 
    'A', 'G', 'M', 
    'Y', 'F', 'P', 
    'D', 'X', 'B', 
    'N', 'J', 'Z', 
    'S', 'Q', 'V', 
    'H', 'L', 'C', 
    'K', 'E'
)

try:
    dni = int(input())

    while len(str(dni)) != 8:
        dni = int(input())

    print(LETRAS[dni % 23])

except ValueError:
    print('[!] Debe ser un entero!')