import numpy as np
def submatrix_with_particular_sum(np_matrix):
    return np.where(np_matrix == -64, np_matrix, np.nan).tolist()
