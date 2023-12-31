
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Extract the submatrix
            submatrix = matrix[i:, j:]
            # Calculate the sum of all integers in the submatrix
            submatrix_sum = np.sum(submatrix)
            # Check if the sum equals -15
            if submatrix_sum == -15:
                # Add the submatrix to the result list
                result.append(submatrix)
    # Return the result list
    return result
