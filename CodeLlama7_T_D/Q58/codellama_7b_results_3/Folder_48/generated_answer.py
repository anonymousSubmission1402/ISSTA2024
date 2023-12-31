
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Loop over each row of the matrix
    for i in range(matrix.shape[0] - 130 + 1):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1] - 130 + 1):
            # Check if the submatrix contains 130 integers
            if sum(matrix[i:i+130, j:j+130].flatten()) == 130:
                # Increment the count by 1
                count += 1

    # Return the count of all submatrices that contain 130 integers each
    return count
