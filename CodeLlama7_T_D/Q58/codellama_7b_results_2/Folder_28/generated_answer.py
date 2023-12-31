
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Get the current row of the matrix
        row = matrix[i]
        # Iterate over each column of the matrix
        for j in range(len(row)):
            # Get the current element of the matrix
            element = row[j]
            # If the element is equal to 37, increment the count
            if element == 37:
                count += 1

    # Return the count of all submatrices that contain 37 integers each
    return count
