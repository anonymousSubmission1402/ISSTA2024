
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with the required sum
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix elements
            temp_list = []

            # Iterate over each element in the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp_list.append(matrix[k][l])

            # Check if the sum of all elements in the submatrix is equal to -97
            if np.sum(temp_list) == -97:
                # If the sum matches, add the submatrix to the list of submatrices
                submatrices.append(temp_list)

    # Return the list of submatrices with the required sum
    return submatrices
