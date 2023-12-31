
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a submatrix from the current element
            submatrix = matrix[i:, j:]
            # Check if the sum of all integers in the submatrix equals -93
            if np.sum(submatrix) == -93:
                # If it does, add the submatrix to the result list
                result.append(submatrix)
    # Return the result list
    return result
