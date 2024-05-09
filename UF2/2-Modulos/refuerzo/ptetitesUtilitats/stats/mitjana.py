import stats.utils

def mitjana():
    nums = stats.utils.getArrayOfNums()
    print(calcularMitjana(nums))
    input('ENTER per continuar')

def calcularMitjana(nums):
    return sum(nums) / len(nums)