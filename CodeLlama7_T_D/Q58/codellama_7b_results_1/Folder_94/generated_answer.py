
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 93 integers each
    count = 0
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 93
            if matrix[i, j] == 93:
                # Initialize a counter variable to keep track of the number of elements in the submatrix
                counter = 0

                # Iterate over each element in the submatrix
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        # Check if the current element is equal to 93
                        if matrix[k, l] == 93:
                            # Increment the counter variable
                            counter += 1

                # Check if the counter variable is equal to 93
                if counter == 93:
                    # Increment the count of submatrices with 93 integers each
                    count += 1

    # Return the count of submatrices with 93 integers each
    return count
