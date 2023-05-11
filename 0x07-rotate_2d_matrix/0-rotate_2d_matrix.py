#!/usr/bin/env python3
'''
To rotate the matrix by 90 degrees clockwise, we can follow the below approach:

1. Transpose the matrix i.e. swap the elements along the diagonal
2. Reverse each row of the transposed matrix
'''


def rotate_2d_matrix(matrix):
    '''transpose matrix'''
    matx = len(matrix)

    for i in range(matx):
        for j in range(i, matx):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matx):
        matrix[i] = matrix[i][::-1]
