
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # Initialize a counter variable to keep track of the number of integers in the submatrix
            counter = 0

            # Loop through each element of the submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if matrix[k][l] == 24:
                        counter += 1

                    if counter == 24:
                        count += 1

                    if count > 0:
                        break

            # If the submatrix contains 24 integers, increment the count variable
            if counter == 24:
                count += 1

            # If the count variable is greater than 0, break out of the loops
            if count > 0:
                break

    # Return the count variable
    return count
