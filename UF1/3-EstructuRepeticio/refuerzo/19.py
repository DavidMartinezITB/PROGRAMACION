"""
    # David Martinez - ASIXc1A
    # 11/12/2023
    # M03 UF1 - Estructures de repeticio
    # Descripcion: 

    Escriu un programa que mostri el següent menú d’opcions:
    Literatura
    Cinema
    Música
    Videojocs
    Sortir
    Si l’usuari tria una opció de l’1 al 4, el programa ha de mostrar uns quants suggeriments de títols relacionats amb el tema escollit. Si l’usuari tria una opció no contemplada, el programa ha de mostrar un missatge d’error. En tot cas, el programa tornarà a mostrar el menú d’opcions, tret que l’usuari triï l’opció 5: en aquest cas, el programa mostrarà un missatge de comiat i acabarà.
"""

MENU = """1. Literatura
2. Cinema
3. Música
4. Videojocs
5. Sortir
"""

enabled = True

while enabled:
    print(MENU)
    match input('-> '):
        case '1': 
            print('Ni idea de literatura :=)\n')
        case '2': 
            print('Los pinguinos de Madagascar (nunca supe como se escribia)\n')
        case '3': 
            print('tengo un tractor amarillo\n')
        case '4': 
            print('fornite minecra fifa\n')
        case '5': 
            enabled = False
        case _:
            print('Error: Caso no contemplado!\n')

print('Adeu!')