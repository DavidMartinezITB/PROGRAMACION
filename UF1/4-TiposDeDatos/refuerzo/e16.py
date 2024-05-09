MENU = """
[1] - Añadir numero al final de la lista
[2] - Añadir numero en una posicion de la lista
[3] - Muestra la longitud de la lista
[4] - Muestra y suprime el ultimo numero de la lista
[5] - Suprime el numero en una posicion especifica
[6] - Cuenta repeticiones de numeros en la lista
[7] - Muestra donde se encuentran todas las coincidencias de un numero (posiciones)
[8] - Muestra la lista
[9] - Salir"""

num_list = []

print(MENU)
select = input()

while select != '9':
    match select:
        case '1':
            num_list.append(input(' (valor) -> '))
        case '2':
            num_list.insert(input(' (pos) -> '), input(' (valor) -> '))
        case '3':
            print(' La lista contiene {} valores'.format(len(num_list)))
        case '4':
            print(' El ultimo numero es el {}'.format(num_list[-1]))
            num_list.pop(-1)
        case '5':
            pos = input(' (pos) -> ')
            