"""
David Martinez - ASIXc1A
M03 - Programacio

SWAP
"""

LEN = 4
try:
    nums = [int(x) for x in input().split()]

    if len(nums) == LEN:
    #     nums[0], nums[-1] = nums[-1], nums[0]
    #     print(nums)
    
    #   Sin usar el swap de py
        new_nums = []
        
        new_nums.append(nums[-1])

        for i in range(1, len(nums) - 1):
            new_nums.append(nums[i])
        
        new_nums.append(nums[0])

        print(new_nums)
    else:
        print(f'[!] Deben ser exactamente {LEN} numeros!')
    
    
except ValueError:
    print('[!] Solo se aceptan enteros!')