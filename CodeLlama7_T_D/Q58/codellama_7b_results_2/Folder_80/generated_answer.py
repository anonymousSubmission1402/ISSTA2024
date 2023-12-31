
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 180 + 1):
        for j in range(matrix.shape[1] - 180 + 1):
            submatrix = matrix[i:i+180, j:j+180]
            if np.count_nonzero(submatrix) == 180:
                count += 1
    return count
