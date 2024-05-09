from random import randint

LEN = 10
RANGE = [1, 10]

nums = []

for i in range(LEN):
    nums.append(randint(RANGE[0], RANGE[1]))

nums.sort()

print(nums)