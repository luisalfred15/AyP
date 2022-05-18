matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_r = []

scalar = int(input('Please enter a number: '))

for i in matrix:
    j_line_matrix_r = []
    for j in i:
        j_line_matrix_r.append(int(scalar) * j)
    matrix_r.append(j_line_matrix_r)

print(matrix_r)
        