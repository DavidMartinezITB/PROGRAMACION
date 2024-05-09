MENU = """[1] Cuenta las veces que aparece una cadena
[2] Substituye una cadena por el valor de otra
[3] Suprime una cadena de la lista
[4] Muestra la lista
[5] Salir"""

CONTINUE_MSG = '\nPulsa ENTER para continuar...'

values = [i for i in input('Valores de la lista:\n').split()]
running = True
opt = '0'

if values != []:
    while running and opt != '5':
        print('\033c', MENU, sep='')
        print(values)
        try:
            opt = input(' -> ')
            match opt:
                case '1':
                    string = input(' (string)-> ')
                    reps_count = 0
                    for value in values:
                        if value == string:
                            reps_count += 1
                    print(' Coincidencias con {}: {}'.format(string, reps_count))
                case '2':
                    string1 = input(' (string1)-> ')
                    string2 = input(' (string2)-> ')
                    for i in range(len(values)):
                        if values[i] == string1:
                            values[i] = string2
                case '3':
                    string = input(' (string)-> ')
                    if string in values:
                        remove_values = []
                        for i in range(len(values)):
                            if values[i] == string:
                                remove_values.append(values[i])
                        values = [i for i in values if i not in remove_values]
                    else:
                        print(' [!] No se encontraron coincidencias!')
                case '4':
                    print(' ', values)
                case '5':
                    print('\nSaliendo...')
            
            if opt != '5':
                input(CONTINUE_MSG)
        except KeyboardInterrupt:
            opt = '0'
else:
    print('[!] La lista no puede estar vacia!')