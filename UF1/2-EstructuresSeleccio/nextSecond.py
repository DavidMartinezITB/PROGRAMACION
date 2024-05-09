"""
    # David Martinez - ASIXc1A
    # 30/10/2023
    # M03 UF1 A3 - Estructures de seleccio
    # Descripcion: 

    L'usuari introdueix una hora amb tres enters (hores, minuts i segons).

    Imprimeix l'hora que serà al cap d'un segon

    Input

    10 50 59


    Output

    10:51:00
"""

try:
    hora, minut, segon = input('').split()
    hora = int(hora)
    minut = int(minut)
    segon = int(segon)
except:
    exit('Error: no has introduit be les dades!')

# Validem que esta dins de rang
if hora >= 24 or hora < 0 or minut >= 60 or minut < 0 or segon >= 60 or segon < 0:
    exit('Hora, minut o segon fora de rang!')

segon += 1

if segon >= 60:
    segon = 0
    minut += 1
    if minut >= 60:
        minut = 0
        hora += 1
        if hora >= 24:
            hora = 0

# Convertim a string
hora = str(hora)
minut = str(minut)
segon = str(segon)

# Si es nomes un digit (1), passem a dos digits amb un 0 davant (01)
if len(hora) == 1:
    hora = '0' + hora
if len(minut) == 1:
    minut = '0' + minut
if len(segon) == 1:
    segon = '0' + segon

print(hora + ':' + minut + ':' + segon)