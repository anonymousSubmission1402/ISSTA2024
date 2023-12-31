
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices with the desired sum
    submatrices = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a list to store the elements of the submatrix
            submatrix_elements = []
            # Loop over each row of the submatrix
            for k in range(i, i + 2):
                # Loop over each column of the submatrix
                for l in range(j, j + 2):
                    # Add the element to the list of elements
                    submatrix_elements.append(matrix[k][l]])
            # Check if the sum of the elements is equal to -46
            if sum(submatrix_elements) == -46:
                # If it is, add the submatrix to the list of submatrices with the desired sum
                submatrices.append(submatrix_elements)
    # Return the list of submatrices with the desired sum
    return submatrices
