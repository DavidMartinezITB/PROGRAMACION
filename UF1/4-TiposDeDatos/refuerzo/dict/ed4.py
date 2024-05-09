
notes = {}

try:
    alumn_amount = int(input('Cantidad de alumnos: '))
    
    count = 0
    while count != alumn_amount:
        name = input('Nombre del alumno: ').lower()
        if name not in notes:
            count += 1
            notes[name] = []
            print('Introduce las notas de {} (para indicar fin, introducimos numero negativo): '.format(name.capitalize()))
            note = int(input())
            while note >= 0:
                if note >= 0 and note <= 10:
                    notes[name].append(note)
                else:
                    print('[!] Rango valido de notas del 0 al 10!')
                note = int(input())
        else:
            print('[!] El alumno ya existe')

    print(notes)
except ValueError:
    print('[!] Error de tipo de datos!')
except KeyboardInterrupt:
    print()
    print(notes)
    print('Saliendo...')