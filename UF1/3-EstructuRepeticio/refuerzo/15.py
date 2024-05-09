STARTING = 10
MESES = 20

current = STARTING / 2
each_month = []

for i in range(MESES):
    current *= 2
    each_month.append(current)

for k, v in enumerate(each_month):
    k = str(k+1)
    if len(k) == 1: k = '0' + k
    print(f'{k} -> {round(v)}€')

print(f'\nTotal -> {sum(each_month)}€')