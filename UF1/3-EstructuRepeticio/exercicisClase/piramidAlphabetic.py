"""
    # David Martinez - ASIXc1A
    # 27/11/2023
    # M03 UF1 - Estructures de repeticio
    # Descripcion: 

    Imprimir de la A fins la Z.

    A cada linia apareix un carcater i la seguent linia apareix un carcater més de forma progresiva. Fins aconseguir tenir una linia que mostri de la A fins la Z

    Output

    A 
    A B 
    A B C 
    ...
"""
# import string

## Obtenemos el abecedario en mayusculas
# abc = string.ascii_uppercase

## Inicializamos la variable que formatearemos con las letras separadas por espacios
# abcF = ''

## Separamos las letras por espacios
# for i in range(len(abc)):
    # abcF = abcF + abc[i] + ' '

## Jugamos con el rango del 1 a la longitud del string, con saltos de dos en dos
# for i in range(1, len(abcF) + 1, 2):
    # print(abcF[:i].strip())

## abcF: abc formateada :)
## Con strip() eliminamos el espacio final que se queda en cada linea



for i in range(ord('A'), ord('Z')):
    for j in range(ord('A'), i + 1):
        print(chr(j), end=' ')
    print()