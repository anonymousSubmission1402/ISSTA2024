
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a count variable to keep track of the number of submatrices with 41 integers
    count = 0
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 41
            if matrix[i, j] == 41:
                # If it is, check if there are at least 41 elements in the submatrix that starts at (i, j) and has a size of 3x3
                if np.sum(matrix[i:i+3, j:j+3]) == 41 * 9:
                    count += 1
    
    # Return the number of submatrices with 41 integers
    return count
