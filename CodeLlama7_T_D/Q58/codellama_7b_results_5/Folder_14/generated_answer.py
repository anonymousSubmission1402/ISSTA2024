
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 84 integers each to 0
    count = 0

    # Iterate over the rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the submatrix starting at (i, j) has 84 integers each
            if np.sum(matrix[i:i+84, j:j+84]) == 84:
                # Increment the count of submatrices with 84 integers each
                count += 1

    return count
