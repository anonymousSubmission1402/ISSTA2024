
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []

    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[0])):
            # Calculate the sum of all integers in the submatrix starting from (i, j)
            current_sum = np.sum(matrix[i:, j:])

            # If the sum is equal to 41, add the submatrix to the result list
            if current_sum == 41:
                result.append((i, j))

    return result
