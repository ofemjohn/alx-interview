#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    '''rotates a 2D matrix.'''
    m = len(matrix)

    # Transpose the matrix
    for i in range(m):
        for j in range(i, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(m):
        matrix[i] = matrix[i][::-1]
