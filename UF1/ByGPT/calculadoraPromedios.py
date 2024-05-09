"""
David Martinez
ASIXc1A


¡Por supuesto! Aquí tienes un ejercicio:

Ejercicio: Calculadora de Promedio

Crea un programa en Python que solicite al usuario ingresar una lista de números. Luego, calcula y muestra el promedio de esos números. Además, indica cuántos de esos números son mayores que el promedio.

Requisitos:

Utiliza un bucle para ingresar los números.
Usa una estructura de control if para determinar si cada número es mayor que el promedio.
Al final, muestra el promedio y la cantidad de números que son mayores que el promedio.
"""

NUMS = 5
nums = []

def getPromedio(array):
    if len(array) != 0 and isinstance(array, list):
        suma = 0
        for i in array:
            suma += i
        
        return suma / len(array)
    else:
        return 0

try:
    for i in range(NUMS):
        nums.append(float(input()))
    
    promedio = getPromedio(nums)
    print(f'Promedio: {promedio}')

    for i in nums:
        if i > promedio:
            print(f'El numero {i} es mayor al promedio')

except ValueError:
    print('Solo numeros!')