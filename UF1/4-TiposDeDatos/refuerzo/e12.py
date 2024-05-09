LENS = [3, 50]

matrix = [[] for i in range(LENS[0])]

# Create the table using if's to check each position and decide if 0 or 1
for i in range(LENS[0]):
    for j in range(LENS[1]):
        if i == 0 or i == LENS[0] - 1 or j == 0 or j == LENS[1] - 1:
            matrix[i].append(1)
        else:
            matrix[i].append(0)

# Display the matrix as a table
for i in matrix:
    for j in i:
        print(j, end='')
    print()