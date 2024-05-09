import utils, stats.mitjana, stats.mediana, stats.desviacion_est, strings.cesar, strings.palindrom, strings.crazyWords.crazy_words


def getOpt(display):
    utils.cls()
    print(display)
    return input(' -> ')

def menu():
    opt = ''
    while opt != '3':
        opt = getOpt('Petites utilitats\n[1] Utilitats estadistiques\n[2] Utilitats de cadenes\n[3] Sortir')
        match opt:
            case '1':
                menuStats()
            case '2':
                menuStrings()
            case '3':
                print('ADEU!')
            case _:
                print('[!] Opcion no valida')
                input('ENTER per continuar')

def menuStats():
    opt = ''
    while opt != '4':
        opt = getOpt('Utilitats estadistiques\n[1] Calcular mitjana\n[2] Calcular mediana\n[3] Calcular desviacio estandard\n[4] Torna enrere')
        utils.cls()
        match opt:
            case '1':
                stats.mitjana.mitjana()
            case '2':
                stats.mediana.mediana()
            case '3':
                stats.desviacion_est.desviacion_est()
            case '4':
                print('ADEU!')
            case _:
                print('[!] Opcion no valida')
                input('ENTER per continuar')

def menuStrings():
    opt = ''
    while opt != '4':
        opt = getOpt('Utilitats de cadenes\n[1] Crazy Words\n[2] Palindroms\n[3] Xifratge de cesar\n[4] Torna enrere')
        utils.cls()
        match opt:
            case '1':
                strings.crazyWords.crazy_words.crazy_words()
            case '2':
                strings.palindrom.palindrom()
            case '3':
                strings.cesar.cesar()
            case '4':
                print('ADEU!')
            case _:
                print('[!] Opcion no valida')
                input('ENTER per continuar')