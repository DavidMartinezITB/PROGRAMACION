"""
    # David Martinez - ASIXc1A
    # 24/11/2023
    # M03 UF1 - Estructures de repeticio
    # Descripcion: 

    Imprimeix les taules de multiplicar en forma de taula.

    PISTA: Amb un print(...) només també es podria fer. Però hem vingut a jugar. Dedicar a "Souli" Soulaimane

    output

    1  2  3  4  5  6  7  8  9
    2  4  6  8 10 12 14 16 18
    3  6  9 12 15 18 21 24 27
    4  8 12 16 20 24 28 32 36
    5 10 15 20 25 30 35 40 45
    6 12 18 24 30 36 42 48 54
    7 14 21 28 35 42 49 56 63
    8 16 24 32 40 48 56 64 72
    9 18 27 36 45 54 63 72 81
"""

for i in range(1, 10):
    for j in range(1, 10):
        res = str(i * j)
        
        # Si solo hay un numero (1 - 9), me añades un espacio para que quede bonico
        if len(res) == 1 and j != 1:
            res = ' ' + res
        
        # Evitamos que al final de cada linea haya un espacio en blanco innecesario, y hacemos el salto de linea para la siguiente tabla
        if j != 9:
            print(res, end=' ')
        else:
            print(res)

# ¿xd?
# print("""
# 1  2  3  4  5  6  7  8  9
# 2  4  6  8 10 12 14 16 18
# 3  6  9 12 15 18 21 24 27
# 4  8 12 16 20 24 28 32 36
# 5 10 15 20 25 30 35 40 45
# 6 12 18 24 30 36 42 48 54
# 7 14 21 28 35 42 49 56 63
# 8 16 24 32 40 48 56 64 72
# 9 18 27 36 45 54 63 72 81
# """)