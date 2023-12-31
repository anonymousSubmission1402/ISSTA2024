
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a list to store the elements of the submatrix
            submatrix = []

            # Add the elements of the submatrix to the list
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if row < matrix.shape[0] and col < matrix.shape[1]:
                        submatrix.append(matrix[row][col])

            # Check if the sum of all elements in the submatrix is equal to 2
            if sum(submatrix) == 2:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that satisfy the condition
    return submatrices
