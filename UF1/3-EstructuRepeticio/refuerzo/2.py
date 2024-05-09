"""
    # David Martinez - ASIXc1A
    # 11/12/2023
    # M03 UF1 - Estructures de repeticio
    # Descripcion: 

    Crea una aplicació que permet endevinar un número. L'aplicació genera un nombre “aleatori” de l'1 al 100. A continuació, l’aplicació va demanant números i va responent si el nombre a endevinar és més gran o més petit que el que ha introduït, a més dels intents que et queden (tens 10 intents per encertar-lo). El programa acaba quan s'encerta el número (a més et diu quants intents has necessitat per encertar-lo), si s'arriba al límit d'intents, l’aplicació et mostra el número que havia generat.
"""

import random

MAX_INTENTS = 10 # Constante que define los intentos disponibles

intents = MAX_INTENTS # Contador

num = random.randint(1, 100)
print(f'Debug: el numero random es {num}')

try:
    inputNum = int(input())

    while intents != 1 and num != inputNum:
        intents -= 1
        print(f'Te quedan {intents} intentos')
        if inputNum > num:
            print('El numero introduit es mes gran que el numero generat')
            inputNum = int(input())
        elif inputNum < num:
            print('El numero introduit es mes petit que el numero aleatori')
            inputNum = int(input())

    if num == inputNum:
        print(f'Lo has adivinado despues de {(MAX_INTENTS + 1) - intents} intentos')
    else:
        print('No has podido averiguarlo')
except ValueError:
    print('SOLO SE ACEPTAN ENTEROS!')