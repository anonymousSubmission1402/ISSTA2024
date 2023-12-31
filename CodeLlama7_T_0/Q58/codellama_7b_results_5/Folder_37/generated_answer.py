
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 64 + 1):
        for j in range(matrix.shape[1] - 64 + 1):
            if np.all(matrix[i:i+64, j:j+64] == 1):
                count += 1
    return count
