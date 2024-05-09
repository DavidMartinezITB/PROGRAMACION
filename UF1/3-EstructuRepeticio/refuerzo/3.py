nums = []

inputNum = 1

while inputNum != 0:
    inputNum = int(input())
    if inputNum != 0:
        nums.append(inputNum)

# Sacamos la suma
suma = 0

for i in nums:
    suma += i

# Sacamos media
media = suma / len(nums)

print(f'Suma: {suma}')
print(f'Media: {media}')