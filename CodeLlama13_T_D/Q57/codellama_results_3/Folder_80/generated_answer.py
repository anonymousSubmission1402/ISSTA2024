
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices with the required sum
    submatrices = []
    
    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_matrix = np.zeros((3, 3), dtype=int)
            
            # Fill the temporary matrix with the elements of the current submatrix
            for k in range(3):
                for l in range(3):
                    temp_matrix[k, l] = matrix[i + k, j + l]
                    
            # Check if the sum of all integers in the temporary matrix is 245
            if np.sum(temp_matrix) == 245:
                # If so, add the temporary matrix to the list of submatrices
                submatrices.append(temp_matrix)
                
    # Return the list of all submatrices with the required sum
    return submatrices
