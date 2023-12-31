
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    output = []
    for size in range(1, min(rows, cols) + 1):
        for x in range(0, rows - size + 1):
            for y in range(0, cols - size + 1):
                submatrix = matrix[x:x + size, y:y + size]
                if np.sum(submatrix) == 752:
                    output.append(submatrix)
    return output
