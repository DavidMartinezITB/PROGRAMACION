"""
David Martinez
ASIXc1A


¡Por supuesto! Aquí tienes otro ejercicio:

Ejercicio: Conversión de Temperatura

Crea un programa en Python que solicite al usuario ingresar una temperatura en grados Celsius. Luego, convierte esta temperatura a grados Fahrenheit y muestra el resultado. Utiliza la fórmula de conversión:

F = (9 / 5) * C + 32

Donde:

F es la temperatura en grados Fahrenheit.
C es la temperatura en grados Celsius.

Requisitos:

Utiliza una función para realizar la conversión.
Utiliza la función input para obtener la temperatura en grados Celsius del usuario.
Muestra el resultado de la conversión en el formato "X grados Celsius son Y grados Fahrenheit".
"""

def celsiusToFahrenheit(c):
    return (9 / 5) * c + 32
try:
    c = float(input())
    f = celsiusToFahrenheit(c)

    print(f'Celsius\t\t{round(c, 2)}°C')
    print(f'Fahrenheit\t{round(f, 2)}°F')
except ValueError:
    print('Debe ser un numero!')