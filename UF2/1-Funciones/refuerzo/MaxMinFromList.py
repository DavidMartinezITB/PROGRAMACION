def createList():
    try:
        list = [int(x) for x in input().split() ]
        return list
    except: 
        return []

def getMin(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

def getMax(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

list = createList()

if list != []:
    print("Numero menor:\t{}\nNumero mayor:\t{}".format(getMin(list), getMax(list)))
else:
    print('[!] An error has ocurred while creating the list')