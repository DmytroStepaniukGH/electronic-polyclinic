matrix = [[1, 2, 3], [3, 5, 8], [0, 23, 15]]

for i in range(0, len(matrix)):
    for j in range(len(matrix[i])):
        print(f'i = {i}, j = {j}')
        print(f'matrix[{i}][{j}]')
        matrix[i][j] *= 2

print(matrix)