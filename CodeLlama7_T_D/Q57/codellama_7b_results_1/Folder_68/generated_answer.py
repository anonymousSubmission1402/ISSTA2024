
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0
            # Loop over each element of the submatrix
            for k in range(i, i + 2):
                for l in range(j, j + 2):
                    # Add the element to the sum of the submatrix
                    submatrix_sum += matrix[k][l]
            # Check if the sum of the submatrix equals 3
            if submatrix_sum == 3:
                # If yes, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 2, j:j + 2])
    # Return the list of submatrices
    return submatrices
