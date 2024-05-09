q = int(input('Cuantos numeros quieres introducir: '))

nums = []
counts = {
  "mayores que 0": 0,
  "0": 0,
  "menores que 0": 0
}

for i in range(q):
    nums.append(int(input(f'{i + 1}: ')))

for n in nums:
    if n > 0:
        counts["mayores que 0"] += 1
    elif n == 0:
        counts["0"] += 1
    else:
        counts["menores que 0"] += 1

for k, v in counts.items():
    print(f'Hay {v} numeros {k}')