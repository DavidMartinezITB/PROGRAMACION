# Initialize nums list
nums = []

# Set the input variable to 0 (do while:)
num = 0

# While num is not a negative value
while num >= 0:
    # Give me the new num
    try:
        num = int(input())
        # If not a negative value
        if num >= 0:
            # Insert it to list
            nums.append(num)
    except ValueError: # In case user input a non-int value
        num = 0 # Set num to 0
        print('[!] Solo se admiten enteros!')

# Convert the nums list onto a dictionary (it deletes de duplicated values)
nums_unique = dict.fromkeys(nums)

# Convert that dict on a list
nums_unique = list(nums_unique)

print(nums_unique)