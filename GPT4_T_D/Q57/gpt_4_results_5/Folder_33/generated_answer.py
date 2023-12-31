
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape[0], matrix.shape[1]
    result = []
    for row1 in range(rows):
        for row2 in range(row1 + 1, rows + 1):
            for col1 in range(cols):
                for col2 in range(col1 + 1, cols + 1):
                    submatrix = matrix[row1:row2, col1:col2]
                    if np.sum(submatrix) == -811:
                        result.append(submatrix)
    return result
