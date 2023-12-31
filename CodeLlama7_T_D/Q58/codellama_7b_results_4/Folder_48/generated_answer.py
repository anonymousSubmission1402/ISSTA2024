
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 130
            if matrix[i][j] == 130:
                # Increment the count by the number of rows and columns in the submatrix
                count += (matrix.shape[0] - i) * (matrix.shape[1] - j)
    # Return the count
    return count
