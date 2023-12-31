
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 104 integers
    count = 0
    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 104
            if matrix[i,j] == 104:
                # If it is, increment the count of submatrices with 104 integers
                count += 1

    return count
