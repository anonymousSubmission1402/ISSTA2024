
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of the elements in the submatrix
            submatrix_sum = 0
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    submatrix_sum += matrix[k][l]

            # Check if the sum of the elements in the submatrix is equal to 84
            if submatrix_sum == 84:
                # Add the submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 3][j:j + 3]])

    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 84. If no such submatrix is found, the function should return an empty list.
    return submatrices
