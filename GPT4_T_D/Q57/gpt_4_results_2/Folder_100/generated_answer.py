
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    
    for size in range(1, min(rows, cols)+1):
        for row in range(rows-size+1):
            for col in range(cols-size+1):
                submatrix = matrix[row:row+size, col:col+size]
                if np.sum(submatrix) == 28:
                    submatrices.append(submatrix)
                    
    return submatrices
