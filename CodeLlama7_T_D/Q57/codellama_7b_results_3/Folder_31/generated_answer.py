
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row in the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column in the matrix
        for j in range(matrix.shape[1]):
            # Extract the submatrix with sum -44
            if np.sum(matrix[i:, j]) == -44:
                submatrices.append(matrix[i:, j])

    # Return the list of all submatrices with sum -44
    return submatrices
