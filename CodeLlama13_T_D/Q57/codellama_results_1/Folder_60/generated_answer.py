
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []

    # Iterate over each submatrix of the given matrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of all integers in the current submatrix
            current_sum = np.sum(matrix[i:i+2, j:j+2])

            # If the sum is equal to 94, add the submatrix to the results list
            if current_sum == 94:
                results.append(matrix[i:i+2, j:j+2])

    # Return the results list
    return results
