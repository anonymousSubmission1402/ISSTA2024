import numpy as np
def submatrix_with_particular_sum(np_matrix):
    return np.where(np.sum(np_matrix, axis=1) == -811, np_matrix, np.array([]))
