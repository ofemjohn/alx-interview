#!/usr/bin/env python
def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise. The matrix must be edited in-place.
    
    Parameters:
    matrix (list): The 2D matrix to be rotated
    
    Returns:
    None
    """
    try:
        # Check if matrix is not empty
        if not matrix:
            raise ValueError("Matrix cannot be empty")
        
        # Get the length of the matrix
        n = len(matrix)
        
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row of the matrix
        for i in range(n):
            matrix[i] = matrix[i][::-1]
    except ValueError as e:
        # Log the error
        print(f"Error: {e}")