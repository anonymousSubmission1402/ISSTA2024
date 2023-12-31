
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with n numbers to 0
    count = 0
    # Loop over the rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 66
            if matrix[i, j] == 66:
                # Increment the count of submatrices with n numbers
                count += 1

    return count
