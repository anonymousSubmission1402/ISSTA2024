
import numpy as np
def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m-2):
        for j in range(n-2):
            if sum(matrix[i:i+3, j:j+3]) == 38:
                count += 1
    return count
