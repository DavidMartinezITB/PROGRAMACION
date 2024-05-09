from time import sleep

# region Declaració de Funcions ----------
def recopilar_ingredients():
    print("Comprar al supermercat")
    sleep(1)
    print("Disposar-los sobre el marbre")
    sleep(1)

def cuinar_tallarins():
    print()
    print('Preparem l\'aigua')
    print(' Escalfem aigua')
    print(' Li possem sal')
    sleep(1)
    print('Bullim tallarines')
    sleep(1)
    print('Escorrem tallarins')
    sleep(1)
    print('Deixar-les preparades')
    sleep(1)

def cuinar_pastanagues():
    print()
    print('Tallar pastanagues')
    sleep(1)
    print('Fregir pastanagues')
    print(' Preparar paella per fregir')
    print(' Rossejar pastanagues')
    print(' Netejar oli de paella')
    sleep(1)
    print('Deixar pastanagues preparades')
    sleep(1)

def cuinar_cebes():
    print()
    print('Tallar cebes')
    sleep(1)
    print('Fregir cebes')
    print(' Preparar paella per fregir')
    print(' Rossejar cebes')
    print(' Netejar oli de paella')
    sleep(1)
    print('Deixar cebes preparades')
    sleep(1)

def preparacio_final():
    print()
    print('Barrejar ingredients amb salsa yakitori')
    sleep(1)
    print('Saltar ingredients')
    print(' Preparar paella per saltar')
    print(' Cuinar remenant ingredients')
    sleep(1)
    print('Deixar llest per servir')
    sleep(1)
# endregion

# region INICI: Preparar fideus Yakisoba
# recopilar_ingredients()
# cuinar_tallarins()
# cuinar_pastanagues()
# cuinar_cebes()
# preparacio_final()
# endregion

# Realiza una funcion que recoge dos numeros y devuelve el mayor pero sin utilizar funciones de python
def mayor(a, b):
    if a > b:
        return a
    else:
        return b

# Funcion que devuelva la media de N numeros sin utilizar funciones de python
def media(*args):
    suma = 0
    for num in args:
        suma += num
    return suma / len(args)