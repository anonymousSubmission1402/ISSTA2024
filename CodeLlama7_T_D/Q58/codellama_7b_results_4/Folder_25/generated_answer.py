
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 65):
        for j in range(matrix.shape[1] - 65):
            if matrix[i:i + 66, j:j + 66].sum() == 66 * 66:
                count += 1

    return count
