#!/usr/bin/python3
"""
2D Matrix rotation
Matrix transposition approach
"""


def rotate_2d_matrix(matrix):
    """ Rotates n x n 2D matrix 90 decrease clockwise
        in place
        Args:
            - matrix - 2D matrix
    """
    matrix.reverse()
    m_len = len(matrix)
    for i in range(m_len):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)