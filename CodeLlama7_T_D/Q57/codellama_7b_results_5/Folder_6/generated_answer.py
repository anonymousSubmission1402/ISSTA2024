
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            sum = 0

            # Calculate the sum of the elements in the submatrix
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    sum += matrix[row][col]

            # If the sum of the elements in the submatrix is equal to 126, add it to the list of submatrices
            if sum == 126:
                submatrices.append(matrix[i:i + 2, j:j + 2])

    # Return the list of all submatrices that have a sum of 126
    return submatrices
