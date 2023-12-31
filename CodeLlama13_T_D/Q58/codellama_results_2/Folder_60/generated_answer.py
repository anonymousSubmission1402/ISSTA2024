
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 87):
        for j in range(cols - 87):
            submatrix = matrix[i:i + 88, j:j + 88]
            if np.sum(submatrix) == 88 * 88:
                count += 1
    return count
