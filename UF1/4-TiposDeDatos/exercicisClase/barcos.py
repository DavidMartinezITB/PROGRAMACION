raw_input = """x x 0 0 0 0 x
               0 0 x 0 0 0 x
               0 0 0 0 0 0 x
               0 x x x 0 0 x
               0 0 0 0 x 0 0
               0 0 0 0 x 0 0
               x 0 0 0 0 0 0"""

map = []

for i in raw_input.strip().split('\n'):
    map.append(i.split())
    print(i.split())

try:
    target = [int(x) for x in input().split()]

    if len(target) == 2:
        if target[0] >= 0 and target[1] >= 0:
            if map[target[0]][target[1]] == 'x':
                print('TOCADO')
            else:
                print('AGUA')
        else:
            print('[!] Los valores no pueden ser negativos!')
    else:
        print('[!] Solo dos enteros')
except ValueError:
    print('[!] Deben ser enteros!')
except IndexError:
    print('[!] Objetivo no existente!')