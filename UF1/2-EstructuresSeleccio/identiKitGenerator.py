"""
    # David Martinez - ASIXc1A
    # 30/10/2023
    # M03 UF1 A3 - Estructures de seleccio
    # Descripcion: 

    Un grup d'investigadors ens ha demanat un programa per generar retrats robots.

    L'usuari ha d'introduir el tipus de cabells, ulls, nas i boca i s'imprimeix per pantalla un dibuix de com és el sospitós.

    Els cabells poden ser arrissats @@@@@, llisos VVVVV o pentinats XXXXX

    Els ulls poden ser aclucats .-.-., rodons .o-o. o estrellats .*-*.

    El nas pot ser aixafat ..0.., arromangat ..C.. o agilenc ..V..

    La boca pot ser normal .===. , bigoti  .∼∼∼.  o dents-sortides  .www.
"""

cabells = input('\nCabells -> (arrissats / lisos / pentinats)\n  -> ').lower()
match cabells:
    case 'arrissats':       cabells = '@' * 5
    case 'lisos':           cabells = 'V' * 5
    case 'pentinats':       cabells = 'X' * 5
    case _:                 exit('Error: Valor introduit inesperat!')

ulls = input('\nUlls -> (aclucats / rodons / estrellats)\n  -> ').lower()
match ulls:
    case 'aclucats':        ulls = '.-.-.'
    case 'rodons':          ulls = '.o-o.'
    case 'estrellats':      ulls = '.*-*.'
    case _:                 exit('Error: Valor introduit inesperat!')

nas = input('\nNas -> (aixafat / arromangat / agilenc)\n  -> ').lower()
match nas:
    case 'aixafat':         nas = '..0..'
    case 'arromangat':      nas = '..C..'
    case 'agilenc':         nas = '..V..'
    case _:                 exit('Error: Valor introduit inesperat!')

boca = input('\nBoca -> (normal / bigoti / dents-sortides)\n  -> ').lower()
match boca:
    case 'normal':          boca = '.===.'
    case 'bigoti':          boca = '.~~~.'
    case 'dents-sortides':  boca = '.www.'
    case _:                 exit('Error: Valor introduit inesperat!')

print('\n' + cabells + '\n' + ulls + '\n' + nas + '\n' + boca)