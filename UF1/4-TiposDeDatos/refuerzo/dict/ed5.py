MENU = """[1] Añadir / modificar
[2] Buscar
[3] Eliminar
[4] Listar
Para salir, CTRL + C..."""

agenda = {}
running = True

def addModd(name):
    if name in agenda:
        print(' ', agenda[name])
        if input(' (modificar el numero de {}) (s/n)-> '.format(name)).lower() == 's':
            agenda[name] = input(' (nuevo numero)-> ')
    else:
        agenda[name] = input(' (numero de {})-> '.format(name))

def find(string):
    if string == '':
        return
    for i in agenda:
        if i.startswith(string):
            print(' ' + i.capitalize(), agenda[i], sep=' - ')

def deleteFromAgenda(name):
    if not name in agenda:
        print(' [!] No se encontraron coincidencias!')
        return

    if input(' (borrar a {} de la agenda?) (s/n)'.format(name)).lower() == 's':
        del agenda[name]

def showAgenda():
    for i in agenda:
        print(' ' + i.capitalize(), agenda[i], sep=' - ')

try:
    while running:
        print(MENU)
        opt = input(' -> ')
        match opt:
            case '1':
                addModd(input(' (name)-> ').lower())
            case '2':
                find(input('(nombres que comienzan por)-> ').lower())
            case '3':
                deleteFromAgenda(input('(nombre)-> ').lower())
            case '4':
                showAgenda()
except KeyboardInterrupt:
    print('\nSaliendo...')