import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+1] == 78, axis=1) for i in range(0, len(matrix)-77) for j in range(i+1, len(matrix)))
