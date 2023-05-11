## 0x07. Rotate 2D Matrix


Problem Statement
Given an n x n 2D matrix, rotate it 90 degrees clockwise. The matrix must be edited in-place.

Approach
To rotate the matrix by 90 degrees clockwise, we can follow the below approach:

Transpose the matrix i.e. swap the elements along the diagonal
Reverse each row of the transposed matrix
Pseudo Code

```
function rotate_2d_matrix(matrix):
    # Transpose the matrix
    for i from 0 to n-1:
        for j from i to n-1:
            swap(matrix[i][j], matrix[j][i])
    
    # Reverse each row of the transposed matrix
    for i from 0 to n-1:
        for j from 0 to n/2:
            swap(matrix[i][j], matrix[i][n-j-1])
```

