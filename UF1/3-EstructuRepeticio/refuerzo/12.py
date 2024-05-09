MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

res = 0

for k, v in enumerate(MESES):
    res += int(input(f'Cuanto dinero quieres ahorrar en {v.capitalize()}: '))
    print()
    if k != len(MESES) - 1:
        print(f'Llevas {res}€ ahorrados hasta el mes de {MESES[k + 1].capitalize()}')
    else:
        print(f'Al final del año, habras ahorrado {res}€')