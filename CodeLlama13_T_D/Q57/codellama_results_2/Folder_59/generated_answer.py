
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with a particular sum
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix elements
            temp = []
            
            # Loop through each row of the submatrix
            for k in range(i, matrix.shape[0]):
                # Loop through each column of the submatrix
                for l in range(j, matrix.shape[1]):
                    # Add the element at the current position to the temporary list
                    temp.append(matrix[k, l])
            
            # Check if the sum of all elements in the temporary list is equal to 2
            if sum(temp) == 2:
                # If it is, add the submatrix to the list of submatrices with a particular sum
                submatrices.append(np.array(temp).reshape(len(temp), 1))
    
    return submatrices
