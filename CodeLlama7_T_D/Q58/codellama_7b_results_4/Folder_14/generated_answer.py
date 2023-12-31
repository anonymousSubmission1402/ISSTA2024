
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 83):
        for j in range(matrix.shape[1] - 83):
            if matrix[i:i + 84, j:j + 84].sum() == 84 * 84:
                count += 1
    return count
