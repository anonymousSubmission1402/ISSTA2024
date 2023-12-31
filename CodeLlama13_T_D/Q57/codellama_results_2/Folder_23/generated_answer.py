
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over all possible rows of the submatrix
    for row in range(matrix.shape[0]):
        # Iterate over all possible columns of the submatrix
        for col in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_matrix = np.zeros((3, 3), dtype=np.int64)
            
            # Fill the temporary matrix with the values of the original matrix
            for i in range(temp_matrix.shape[0]):
                for j in range(temp_matrix.shape[1]):
                    temp_matrix[i, j] = matrix[row + i, col + j]
            
            # Check if the sum of all integers in the current submatrix is 59
            if np.sum(temp_matrix) == 59:
                # If it is, add it to the result list
                result.append((row, col))
    
    return result
