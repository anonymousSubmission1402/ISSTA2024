
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # Initialize a variable to store the sum of the current submatrix
            submatrix_sum = 0

            # Calculate the sum of the current submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    submatrix_sum += matrix[k][l]

            # Check if the sum of the current submatrix is equal to 997
            if submatrix_sum == 997:
                # Add the current submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 3][j:j + 3]])

    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 997. If no such submatrix is found, the function should return an empty list.
    return submatrices
