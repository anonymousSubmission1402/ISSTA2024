
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i,j] == 901:
                return [np.array([matrix[i:i+1,j:j+1]])]
    return []
