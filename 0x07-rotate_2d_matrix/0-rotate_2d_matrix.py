#!/usr/bin/python3
'''rotate matrix '''


def rotate_2d_matrix(matrix):
    m = len(matrix)

    '''Transpose the matrix'''
    for i in range(m):
        for j in range(i, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    ''' Reverse each row of the transposed matrix'''
    for i in range(m):
        for j in range(m // 2):
            matrix[i][j], matrix[i][m - j -
                                    1] = matrix[i][m - j - 1], matrix[i][j]
