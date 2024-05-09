workers         = int(input('Trabajadores: '))
sueldo_hora     = float(input('Sueldo / hora: '))
data            = []

for i in range(workers):
    # i = str(i)
    # if len(i) == 1: i = '0' + i

    dias = -1
    while dias < 0 or dias > 7:
        dias = int(input(f'[TRABAJADOR {i}] -> Dias trabajados: '))
    
    data.append([])
    for j in range(1, dias + 1):
        data[i].append(int(input(f'[TRABAJADOR {i}] [DIA {j}] -> Horas: ')))
    
    print()

for i in range(len(data)):
    print(f'TRABAJADOR {i}')
    sueldo = 0
    for k, v in enumerate(data[i]):
        print(f'  [DIA {k}]         -> {v * sueldo_hora}€')
        sueldo += v * sueldo_hora
    print(f'  [SUELDO SEMANA] -> {sueldo}€\n')