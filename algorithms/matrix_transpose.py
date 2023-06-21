matrix_list = [
    [1, 'a', 'aa'],
    [4, 'b', 'bb'],
    [7, 'c', 'cc']
]

transposed_matrix = []
for row in range(len(matrix_list)):
    transposed_matrix.append([0] * len(matrix_list[0]))

for i in range(len(matrix_list)):
    for j in range(len(matrix_list[0])):
        transposed_matrix[j][i] = matrix_list[i][j]

print(transposed_matrix)

# one more example
# transposed_matrix = zip(*matrix_list)
# print(transposed_matrix)




