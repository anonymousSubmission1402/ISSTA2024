
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum -13
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix
            temp_mat = np.zeros((matrix.shape[0], matrix.shape[1]), dtype=int)
            
            # Fill the temporary matrix with the elements of the main matrix
            for k in range(temp_mat.shape[0]):
                for l in range(temp_mat.shape[1]):
                    temp_mat[k, l] = matrix[i+k, j+l]
            
            # Check if the sum of all elements in the temporary matrix is equal to -13
            if np.sum(temp_mat) == -13:
                # If so, add the submatrix to the list of submatrices
                submatrices.append(temp_mat)
    
    # Return the list of submatrices with sum -13
    return submatrices
