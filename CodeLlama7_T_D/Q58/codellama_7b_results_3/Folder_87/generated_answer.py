
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 96 integers each
    count = 0

    # Iterate over all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a submatrix with the current row and column
            submatrix = np.array([[matrix[i, j]]])

            # Iterate over all rows and columns of the submatrix
            for k in range(submatrix.shape[0]):
                for l in range(submatrix.shape[1]):
                    # Check if the current element is equal to 96
                    if submatrix[k, l] == 96:
                        # Increment the count of submatrices with 96 integers each
                        count += 1

    # Return the count of all submatrices with 96 integers each
    return count
