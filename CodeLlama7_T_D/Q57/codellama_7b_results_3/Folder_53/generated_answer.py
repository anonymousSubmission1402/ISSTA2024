
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []

    # Loop over all possible submatrix sizes
    for size in range(1, matrix.shape[0] + 1):
        # Get the number of rows and columns in each submatrix
        nrows, ncols = size, size

        # Check if the submatrix is square
        if nrows != ncols:
            continue

        # Loop over all possible starting indices
        for row in range(matrix.shape[0] - nrows + 1):
            for col in range(matrix.shape[1] - ncols + 1):
                # Get the submatrix of interest
                submatrix = matrix[row:row+nrows, col:col+ncols]

                # Check if the sum of all integers in the submatrix is equal to -37
                if np.sum(submatrix) == -37:
                    result.append(submatrix)

        # If a submatrix with the desired sum is found, return it immediately
        if len(result) > 0:
            return result
