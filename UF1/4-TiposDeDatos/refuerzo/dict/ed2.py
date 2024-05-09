sentence = input()

data = {}

for char in sentence:
    if char in data:
        data[char] += 1
    else:
        data[char] = 1

print(data)