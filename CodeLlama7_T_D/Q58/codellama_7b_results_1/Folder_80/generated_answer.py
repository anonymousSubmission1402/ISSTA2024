
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices found
    count = 0
    # Loop over all possible starting positions in the matrix
    for i in range(matrix.shape[0] - 180 + 1):
        for j in range(matrix.shape[1] - 180 + 1):
            # Check if the current submatrix has 180 integers
            if np.count_nonzero(matrix[i:i+180, j:j+180]) == 180:
                count += 1
    return count
