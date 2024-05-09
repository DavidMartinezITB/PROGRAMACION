import signal, sys

banner = """
----------------------
- CALCULADORA PYTHON -
----------------------
Selecciona una opcion:
 [1] - Suma
 [2] - Resta
 [3] - Multiplicacion
 [4] - Division
 [5] - Division entera
 [6] - Modulo
 [0] - Salir

"""

def restart(msg):
    input(f'\n{msg}\n  Pulsa enter para reiniciar...')
    main()

def suma(a, b):
    return f'  {a} + {b} = {float(a) + float(b)}'

def resta(a, b):
    return f'  {a} - {b} = {float(a) - float(b)}'

def multi(a, b):
    return f'  {a} x {b} = {float(a) * float(b)}'

def div(a, b):
    if b == 0:
        restart('Imposible dividir entre 0!')
    return f'  {a} / {b} = {float(a) / float(b)}'

def divInt(a, b):
    if b == 0:
        restart('Imposible dividir entre 0!')
    return f'  {a} // {b} = {float(a) // round(b)}'

def dibMod(a, b):
    if b == 0:
        restart('Imposible dividir entre 0!')
    return f'  {a} mod {b} = {float(a) % float(b)}'

def main():
    print(banner)

    try:
        opt = int(input('  -> '))
    except ValueError:
        restart('Opcion no valida!')
    
    if opt != 0:
        print('  Introduce los numeros: ')
        
        try:
            a, b = float(input('    -> ')), float(input('    -> '))
        except ValueError:
            restart('Solo se admiten valores numericos!')

        match opt:
            case 1: print(suma(a, b))
            case 2: print(resta(a, b))
            case 3: print(multi(a, b))
            case 4: print(div(a, b))
            case 5: print(divInt(a, b))
            case 6: print(dibMod(a, b))
            case   _: restart('Opcion no implementada todavia!')
    else:
        print('\n  Saliendo...\n')

def interrupt(signum, frame):
    print('\nSaliendo...')
    sys.exit(0)

signal.signal(signal.SIGINT, interrupt)

if __name__ == '__main__':
    main()