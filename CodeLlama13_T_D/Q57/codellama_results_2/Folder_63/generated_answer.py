
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Convert the matrix to a 1D array of integers
    flat_array = matrix.flatten()
    
    # Initialize an empty list to store the indices of the elements in the flattened array
    indices = []
    
    # Iterate over the flattened array and check if the sum of the elements from the starting index to each subsequent index is equal to 64
    for i in range(len(flat_array)):
        current_sum = np.sum(flat_array[:i+1])
        if current_sum == 64:
            indices.append(i)
    
    # If no such submatrix is found, return an empty list
    if not indices:
        return []
    
    # Otherwise, return the submatrices of the given matrix with the desired sum
    submatrices = []
    for i in range(len(indices)):
        start_index = indices[i]
        end_index = indices[i+1] if i < len(indices)-1 else None
        submatrix = np.reshape(flat_array[start_index:end_index], (3, 4))
        submatrices.append(submatrix)
    return submatrices
