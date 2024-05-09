"""
    # David Martinez - ASIXc1A
    # 23/10/2023
    # M03 UF1 - Manipulacion de datos
    # Descripcion: Verificar si a todos les toca minimo una galleta
"""

try:
    persones, galetes = input().split()
except:
    exit('No has introduit dos valors!')

try:
    persones = int(persones)
    galetes = int(galetes)
except:
    exit("No has introduit un numero valid!")

if galetes % persones == 0:
    print("Let's eat!")
else:
    print("Let's fight!")