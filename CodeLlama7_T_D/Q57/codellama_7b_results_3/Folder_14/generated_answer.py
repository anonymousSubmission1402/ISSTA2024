
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            sum_of_submatrix = 0
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    sum_of_submatrix += matrix[row][col]
            if sum_of_submatrix == -93:
                submatrices.append([row, row + 1], [col, col + 1]))
    return submatrices
