from random import randint

import math

LEN = 10

list = []

for i in range(LEN):
    list.append(randint(1, 11))

print('Numero\tCuadrado\tCubo')
for i in list:
    print(f'{i}\t{i ** 2}\t\t{i ** 3}')