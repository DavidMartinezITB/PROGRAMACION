LEN = 5

list = []
list2 = []

for i in range(LEN):
    list.append(input())

for i in range(LEN - 1 , -1, -1):
    list2.append(list[i])

print(list, list2, sep='\n')