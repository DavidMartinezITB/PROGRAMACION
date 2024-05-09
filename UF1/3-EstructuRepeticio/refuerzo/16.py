workers         = int(input('Trabajadores: '))
sueldo_hora     = float(input('Sueldo / hora: '))
sueldos         = []

print()

for i in range(workers):
    i = str(i)
    if len(i) == 1: i = '0' + i
    sueldos.append(float(input(f'[TRABAJADOR {i}] -> Numeros de horas trabajadas por semana: ')))

print()

for k,v in enumerate(sueldos):
    k = str(k)
    if len(k) == 1: k = '0' + k
    print(f'TRABAJADOR {k}   -> {v}€')

print(f'TOTAL           -> {sum(sueldos)}€')