
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with sum 2
    submatrices = []

    # Loop over all possible starting indices for the submatrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of the elements in the submatrix
            submatrix_sum = matrix[i:i+2, j:j+2].sum()

            # If the sum of the elements in the submatrix is equal to 2, add it to the list of submatrices with sum 2
            if submatrix_sum == 2:
                submatrices.append(matrix[i:i+2, j:j+2])

    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 2
    return submatrices
