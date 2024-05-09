RANGO = [1, 5]

for i in range(RANGO[0], RANGO[1] + 1):
    print(f'TABLA DEL {i}')
    print('------------------------')
    for j in range(11):
        print(f'{i} x {j} = {i * j}')
    print()