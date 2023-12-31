
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = matrix.copy()

            # Remove the rows and columns that are outside of the current row and column
            submatrix = np.delete(submatrix, slice(i, None), axis=0)
            submatrix = np.delete(submatrix, slice(None, j+1), axis=1))

            # Check if the sum of all integers in the submatrix is equal to 34
            if submatrix.sum() == 34:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that meet the condition
    return submatrices
