
import numpy as np
def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            submatrix = matrix[i:i+2, j:j+2]
            if np.sum(submatrix) == -20:
                result.append(submatrix)
    return result
