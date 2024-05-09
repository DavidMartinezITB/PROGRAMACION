"""
    # David Martinez - ASIXc1A
    # 2/10/2023
    # M03 UF1 A2 - Manipulacion de datos
    # Descripcion: Averigua si una persona ha celebrado su cumpleaños a partir del mes y dia actual y el del cumpleaños
"""

# Definimos las variables del dia del cumple
diaAniversari = int(input("¿Que dia es tu cumpleaños? "))
mesAniversari = int(input("¿En que mes es tu cumpleaños? "))

# Definimos las variables del dia de hoy
diaActual = int(input("¿Que dia es hoy? "))
mesActual = int(input("¿En que mes estamos? "))

# Realizamos las operaciones logicas
if mesActual >= mesAniversari and diaActual > diaAniversari:
    print("Celebrado!")
elif mesActual == mesAniversari and diaActual == diaAniversari:
    print("Felicidades :)")
else:
    print("No celebrado!")

""" EXPLICACION IF
# Si el mes actual es mayor o igual al mes del cumple Y el dia actual es mayor al dia del cumple:
    # Decimos que lo ha celebrado ya

# De lo contrario, si el mes actual y el dia actual coinciden con el dia y el mes del cumple
    # Felicitamos al usuario, ya que hoy es el dia de su cumpleaños

# En caso contrario, es decir, que ninguna de las operaciones anteriores resulte cierta
    # Decimos que el cumpleaños no ha sido celebrado aun
"""