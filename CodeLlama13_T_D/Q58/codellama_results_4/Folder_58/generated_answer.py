
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 184):
        for j in range(matrix.shape[1] - 184):
            if (matrix[i:i+185,j:j+185] == 1).all():
                count += 1
    return count
