
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 5):
        for j in range(len(matrix[i]) - 5):
            if (matrix[i:i+6,j:j+6]).sum() == 66:
                count += 1
    return count
