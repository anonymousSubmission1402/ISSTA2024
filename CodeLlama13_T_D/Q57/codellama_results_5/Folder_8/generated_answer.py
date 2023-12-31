
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Create a copy of the input matrix
    matrix = np.copy(matrix)
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each element in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the sum of all elements in the submatrix starting from (i, j) is equal to -61
            if np.sum(matrix[i:, j:]) == -61:
                # If yes, add the submatrix to the result list
                result.append((i, j))
    
    return result
