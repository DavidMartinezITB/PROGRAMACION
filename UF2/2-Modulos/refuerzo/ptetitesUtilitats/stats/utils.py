def getArrayOfNums():
    nums = []
    while len(nums) == 0:
        try:
            nums = [int(x) for x in input('Numeros separados por espacios: ').split()]
        except:
            print('[!] Deben ser numeros!')
    return nums