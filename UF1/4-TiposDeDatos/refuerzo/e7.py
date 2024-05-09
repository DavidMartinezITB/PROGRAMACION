LEN = 5

lista1 = []
lista2 = []
lista3 = []

try:
    for i in range(LEN):
        lista1.append(int(input('Lista 1 -> ')))
        lista2.append(int(input('Lista 2 -> ')))
        print()

    for i, j in zip(lista1, lista2):
        lista3.append(i + j)

    # for i, j, k in zip(lista1, lista2, lista3):
    #     print(i, j, k, sep='\t')

    print(lista1, lista2, lista3, sep='\n')
except ValueError:
    print('[!] Solo enteros!')