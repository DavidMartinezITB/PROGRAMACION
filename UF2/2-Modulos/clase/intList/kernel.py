def readIntListFromKeyboard():
    numbers = [int(x) for x in input().split()]
    
    if numbers == [-1]:
        numbers = []
    
    while numbers[-1] != -1:
        numbers += [int(x) for x in input().split()]
    
    return numbers[:-1]