import stats.utils

def mediana():
    nums = stats.utils.getArrayOfNums()
    if len(nums) % 2 != 1:
        # mid_nums = [int(x) for x in nums[len(nums) // 2:len(nums) // 2 + 1]]
        mid_nums = nums[len(nums) // 2 - 1:len(nums) // 2 + 1]
        med = sum(mid_nums) / len(mid_nums)
    else:
        med = nums[len(nums) // 2]
    print(med)
    input('ENTER per continuar')