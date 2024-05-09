num = 1
nums = []

sumNums = 0
outOf = 0
equalsBorders = False

# Emulating a 'do while' in python :(
li, ls = 2, 1

while li > ls:
    li = int(input('Limite inf: '))
    ls = int(input('Limite sup: '))

while num != 0:
    num = int(input())
    if num != 0:
        nums.append(num)

for i in nums:
    # suma
    sumNums += i

    # out of range
    if i not in range(li, ls):
        outOf += 1
    
    if i == li or i == ls:
        equalsBorders == True