valors = [-1, -1]

try:
    while len(valors) != 2 or valors[0] < 0 or valors[1] < 0:
        valors = [int(x) for x in input('BASE EXPONENTE\n').split()]

    b, x = valors[0], valors[1]

    res = 1

    for i in range(x):
        res *= b

    print(res)  
except ValueError:
    print('Deben ser dos enteros')