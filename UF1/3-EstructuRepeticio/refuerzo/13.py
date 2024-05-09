try:
    sueldo = float(input('Sueldo/hora: '))

    if sueldo > 0:
        horasDias = 0

        for i in range(1, 7):
            horas = -1
            while horas > 24 or horas < 0:
                horas = int(input(f'Cuantas horas se ha trabajado el dia {i}? '))
                horasDias += horas

        print(f'Horas trabajadas: {horasDias}')
        print(f'Sueldo semanal: {horasDias * sueldo}€')
    else:
        print('ESCLAVITUD?')
except ValueError:
    print('DEBE SER ENTERO O FLOAT!')