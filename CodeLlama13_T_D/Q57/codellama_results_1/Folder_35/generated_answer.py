
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 432:
                continue
            submatrices = []
            for k in range(i+1, rows):
                for l in range(j+1, cols):
                    if matrix[k][l] == 432:
                        submatrix = np.array([
                            [matrix[m][n] for n in range(j)] + [matrix[m][l] for m in range(i, k+1)],
                            [matrix[m][n] for n in range(j, l+1)]
                        ])
                        submatrices.append(submatrix)
    return submatrices
