import stats.mitjana, stats.utils

def desviacion_est():
    nums = stats.utils.getArrayOfNums()
    mitjana = stats.mitjana.calcularMitjana(nums)
    suma_cuadrats_diferencies = sum((x - mitjana) ** 2 for x in nums)
    varianza = suma_cuadrats_diferencies / len(nums)
    print(varianza ** 0.5)
    input('ENTER per continuar')