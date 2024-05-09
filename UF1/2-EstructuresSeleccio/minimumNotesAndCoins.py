"""
    # David Martinez - ASIXc1A
    # 27/10/2023
    # M03 UF1 A2 - Manipulacion de datos
    # Descripcion: Digues quants bitllets i monedes es necessiten exactament per cobrir la 
                   quantitat introduida per pantalla
"""

try:
    n = float(input('Quantitat: '))
except:
    exit('No has introduit un numero valid!')

quinientos = n // 500
n = n - 500 * quinientos
doscientos = n // 200
n = n - 200 * doscientos
cien = n // 100
n = n - 100 * cien
cincuenta = n // 50
n = n - 50 * cincuenta
diez = n // 10
n = n - 10 * diez
cinco = n // 5
n = n - 5 * cinco
euro = n // 1
n = n - 1 * euro
cent50 = n // .5
n = n - .5 * cent50
cent20 = n // .2
n = n - .2 * cent20
cent10 = n // .1
n = n - .1 * cent10
cent5 = n // .05
n = n - .05 * cent5
cent2 = n // .02
n = n - .02 * cent2
cent1 = n // .01
n = n - .01 * cent1

# Si no es 0, l'imprimim, per cada cas:
if quinientos != 0: print(str(round(quinientos)) + ' billetes de 500€')
if doscientos != 0: print(str(round(doscientos)) + ' billetes de 200€')
if cien != 0: print(str(round(cien)) + ' billetes de 100€')
if cincuenta != 0: print(str(round(cincuenta)) + ' billetes de 50€')
if diez != 0: print(str(round(diez)) + ' billetes de 10€')
if cinco != 0: print(str(round(cinco)) + ' billetes de 5€')
if euro != 0: print(str(round(euro)) + ' monedas de 1€')
if cent50 != 0: print(str(round(cent50)) + ' monedas de 50 centimos')
if cent20 != 0: print(str(round(cent20)) + ' monedas de 20 centimos')
if cent10 != 0: print(str(round(cent10)) + ' monedas de 10 centimos')
if cent5 != 0: print(str(round(cent5)) + ' monedas de 5 centimos')
if cent2 != 0: print(str(round(cent2)) + ' monedas de 2 centimos')
if cent1 != 0: print(str(round(cent1)) + ' monedas de 1 centimo')

## AMB WHILES ##
# # Comprobamos 500
# while n - 500 >= 0:
#     print(n)
#     n -= 500
#     quinientos += 1

# # 100
# while n - 100 >= 0:
#     print(n)
#     n -= 100
#     cien += 1

# # 1
# while n - 1 >= 0:
#     n -= 1
#     euro += 1

# # 0.20
# while n - 0.20 >= 0:
#     n = round(n, 2) - 0.2
#     cent20 += 1

# # 0.10
# while round(n, 3) - 0.10 >= 0:
#     n = round(n, 3) - 0.1
#     cent10 += 1

# # 0.05
# while round(n, 3) - 0.05 >= 0:
#     n = n - 0.05
#     cent5 += 1

# print(quinientos, cien, euro, cent20, cent10, cent5)
# print(round(n, 2))