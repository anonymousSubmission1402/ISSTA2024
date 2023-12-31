
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    submatrices = []

    # Loop over all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = matrix.copy()

            # Remove elements from the copied matrix that are not in the current row or column
            for k in range(submatrix.shape[0]):
                if k != i:
                    submatrix[k] = 0

            # Remove elements from the copied matrix that have a sum different from 34
            for k in range(submatrix.shape[0]):
                if np.sum(submatrix[k]) != 34:
                    submatrix[k] = 0

            # Add the submatrix to the output list if it has a non-zero element
            if np.any(submatrix):
                submatrices.append(submatrix)

    return submatrices
