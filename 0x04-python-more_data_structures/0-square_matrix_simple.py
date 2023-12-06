#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    new_matrix = []
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            row.append(0)
        new_matrix.append(row)

    for i in range(num_rows):
        for j in range(num_cols):
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
