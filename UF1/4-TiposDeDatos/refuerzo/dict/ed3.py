fruits = {
    'pera': 0.6,
    'manzana': 0.4,
    'sandia': 2,
    'melon': 2,
    'fresa': 0.8
}

running = 'y'
while running == 'y':
    try:
        fruit = input('Fruta -> ').lower()

        if fruit in fruits:
            amount = float(input('Cantidad (kg) -> '))
            print('Se han vendido {} kg de {} ({}/kg) por el importe de {}€'.format(amount, fruit, fruits[fruit], round(fruits[fruit] * amount, 2)))
        else:
            print('[!] La fruta no existe!')
        
        running = input('[+] Continuar calculando importes? (y/n)').lower()
    except ValueError:
        print('[!] Debe ser un numero!')
    except KeyboardInterrupt:
        print('\n[!] Saliendo...')
        break