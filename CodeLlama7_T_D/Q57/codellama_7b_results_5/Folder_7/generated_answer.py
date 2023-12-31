
import numpy as np

def submatrix_with_particular_sum(matrix):
    # initialize the output list
    submatrices = []

    # loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # create a submatrix by taking the elements from the current row and column
            submatrix = matrix[i:, j]

            # check if the sum of all integers in the submatrix is equal to -128
            if np.sum(submatrix) == -128:
                # if it is, append the submatrix to the output list
                submatrices.append(submatrix)

    # return the output list of all submatrices that satisfy the condition
    return submatrices
