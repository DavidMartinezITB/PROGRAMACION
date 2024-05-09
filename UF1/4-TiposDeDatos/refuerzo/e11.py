# matrix = [
#     [0] * 5,
# ] * 5

# Set the table lenght
LEN = 10

# Initialize matrix variable filled by 0s
matrix = [ [0] * LEN for i in range(LEN)]

# Iterate the matrix to get the diagonal positions
for row in range(len(matrix)):
    for num in range(len(matrix[row])):
        if row == num or row + num == len(matrix[row]) - 1:
            matrix[row][num] = 1

# Display matrix as a table
for i in matrix:
    for j in i:
        print(j, end=' ')
    print()