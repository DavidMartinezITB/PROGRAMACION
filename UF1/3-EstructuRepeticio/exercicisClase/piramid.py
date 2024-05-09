"""
    # David Martinez - ASIXc1A
    # 27/11/2023
    # M03 UF1 - Estructures de repeticio
    # Descripcion: 

    S'imprimeix una piràmide d'altura N de #

    input

    5


    output

    #
    # #
    # # #
    # # # #
    # # # # # 
"""

# Definimos el caracter que se utilizara
CHARACTER = '❒'

rows = int(input())

for i in range(1, rows + 1):
    line = (CHARACTER + ' ') * i
    print(((CHARACTER + ' ') * i).strip())

# Usamos strip() para eliminar el espacio en blanco sobrante al final de cada