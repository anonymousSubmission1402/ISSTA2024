import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+91] == np.full(91, True), axis=1) for i in range(0, len(matrix)-90) for j in range(i, len(matrix)-90))
