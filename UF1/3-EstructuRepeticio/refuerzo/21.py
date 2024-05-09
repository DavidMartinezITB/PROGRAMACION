from random import randint

INTENTOS    = 10
intentos    = 0

c_num       = 0
c_nums      = []

rango       = [1, 100]

try:
    num = int(input('Numero del 1 al 100: '))

    if num in range(rango[0], rango[1]):
        while intentos != INTENTOS and c_num != num:
            for i in range(INTENTOS):
                c_num = int(randint(rango[0], rango[1]))
                while c_num in c_nums:
                    c_num = randint(rango[0], rango[1])
                
                if c_num != num:
                    intentos += 1
                    c_nums.append(c_num)

                    match input(f'Es mas grande que {c_num}? (S/N) ').lower():
                        case 's':
                            rango[0] = c_num
                        case _:
                            rango[1] = c_num
        if c_num == num:
            print(f'Lo he averiguado despues de {intentos} intentos. Es el {c_num}!')
        else:
            print(f'No lo he podido averiguar :(')
    else:
        print('Numero fuera de rango!') 
except ValueError:
    print('Debe ser int!')