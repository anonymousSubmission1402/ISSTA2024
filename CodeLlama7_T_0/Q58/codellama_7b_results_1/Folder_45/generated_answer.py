
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 28 + 1):
        for j in range(matrix.shape[1] - 28 + 1):
            if np.all(matrix[i:i+28, j:j+28] == 28)):
                count += 1
    return count
