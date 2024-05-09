import ahorcado.ahorcado, buscaminas.buscaminas, hundir_flota.hundir_flota, tres_en_raya.tres_en_raya

def menu():
    MENU = 'JUEGOS!\n [1] Ahorcado\n [2] 3 en Raya\n [3] Buscaminas\n [4] Hundir la flota\n [5] Salir'

    print(MENU)
    return input('-> ')

def whatToPlay(opt):
    match opt:
        case '1':
            ahorcado.ahorcado.play()
        case '2':
            tres_en_raya.tres_en_raya.play()
        case '3':
            buscaminas.buscaminas.play()
        case '4':
            hundir_flota.hundir_flota.play()
        case '5':
            print('Saliendo...')
        case _:
            print('[!] Opcion no valida')