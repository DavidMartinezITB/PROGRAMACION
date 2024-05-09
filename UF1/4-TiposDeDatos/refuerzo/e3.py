LEN = 10
try:
    list = [float(x) for x in input().split() if 0 <= float(x) <= 10]

    # inRange = False

    # for i in list:

    if len(list) == LEN:
        mayor = max(list)
        menor = min(list)
        media = sum(list) / len(list)

        print('Mayor', 'Menor', 'Media', sep='\t')
        print(mayor, menor, media, sep='\t')
    else:
        print('[!] No has introducido 10 numeros del 0 al 10')
except ValueError:
    print('[!] Solo numeros!')