"""
David Martinez - ASIXc1A
M03 Programacion
UF1 - Dades sequencials

LA CASA DE PAPEL
"""
# Numero de cajas disponibles
NUM_CAJAS = 11

# Inicializamos lista con 0s segun la cantidad de cajas disponibles
# cajas = [0 for i in range(NUM_CAJAS)] -> Antiguo
cajas = [0] * NUM_CAJAS

try:
    opens = [int(x) for x in input().split()]

    # Verificamos que los valores estan contemplados entre 0 y el numero total de cajas (que no haya 11 cajas e intenten abrir la caja numero 2223214723498324423)
    okValues = True
    for i in opens[:-1]:
        if i not in range(0, NUM_CAJAS):
            okValues = False

    if len(opens) >= 1 and opens[-1] == -1 and okValues:
        for i in range(len(cajas)):
            for j in opens[:-1]:
                if i == j:
                    cajas[i] += 1
        print(cajas)
    else:
        print('[!] No has introducido correctamente los valores!')
except ValueError:
    print('[!] Solo enteros!')