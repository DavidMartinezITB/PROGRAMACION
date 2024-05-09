MESES = (
    'Enero', 'Febrero', 'Marzo',
    'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre',
    'Octubre', 'Noviembre', 'Diciembre'
)

DIAS = [
    [0, 2, 4, 6, 7, 9, 11], # 30 Dias
    [3, 5, 8, 10] # 31 Dias
]

try:
    mes = int(input()) - 1

    while mes not in range(0, 12):
        mes = int(input(f'[!] No existe el mes numero {mes + 1}\nIntroduce un nuevo mes: ')) - 1

    if mes in DIAS[0]: # 30
        dias = 30
    elif mes in DIAS[1]: # 31
        dias = 31
    else:
        dias = 28
    
    print(f'{MESES[mes]} tiene {dias} dias!')
            
except ValueError:
    print('[!] Debe ser un numero!')