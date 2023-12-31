
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):

        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):

            # Initialize a list to store the elements of the submatrix
            submatrix = []

            # Add the elements of the submatrix to the list
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    submatrix.append(matrix[k][l]])

            # Check if the sum of the elements in the submatrix is equal to 38
            if sum(submatrix) == 38:

                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that satisfy the condition
    return submatrices
