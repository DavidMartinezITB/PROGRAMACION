list = []

try:
    num = int(input())

    while num >= 0:
        list.append(num)
        num = int(input())
    
    if len(list) != 0: print(list)
except ValueError:
    print('[!] Solo numeros enteros!')