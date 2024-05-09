noms    = []
edats   = []

nom = ''

def getMax(edats):
    edatMax = 0
    for edat in edats:
        if edat > edatMax:
            edatMax = edat
    return edatMax


try:
    while nom != '*':
        nom     = input('Nom\t')

        if nom != '*':
            edat = int(input('Edat\t'))
            noms.append(nom)
            edats.append(edat)

    if len(noms) != 0:
        print(noms, edats, sep='\n')
    else:
        print('[!] No se ha recogido ningun alumno!')
    
    print('\nAlumnos mayores de edad:')
    for nom, edat in zip(noms, edats):
        if edat >= 18:
            print(f' - {nom}')
    
    print(f'{getMax(edats}'))
    

except ValueError:
    print('[!] Unicamente edades en numeros enteros!')