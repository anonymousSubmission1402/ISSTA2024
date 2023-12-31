
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Find the submatrix starting from (i, j) and having a size of 3x3
            submatrix = matrix[i:i+3, j:j+3]

            # Check if the sum of all integers in the submatrix is equal to 8
            if np.sum(submatrix) == 8:
                # If the sum is equal to 8, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices with a particular sum
    return submatrices
