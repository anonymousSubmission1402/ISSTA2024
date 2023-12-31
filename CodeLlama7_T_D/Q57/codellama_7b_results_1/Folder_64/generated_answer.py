
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the matrix excluding the current row and column
            submatrix = matrix[:i, :j].copy()

            # Calculate the sum of all integers in the current submatrix
            sum_current_submatrix = np.sum(submatrix)

            # Check if the sum is equal to -4
            if sum_current_submatrix == -4:
                # Add the current submatrix to the result list
                result.append(submatrix)

    # Return the result list
    return result
