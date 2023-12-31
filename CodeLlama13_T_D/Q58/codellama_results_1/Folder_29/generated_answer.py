
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a counter for the number of submatrices found
    count = 0
    
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the current row
        for j in range(len(matrix[i])):
            # Check if the current element is equal to n
            if matrix[i][j] == n:
                # If it is, increment the counter and recursively search the surrounding submatrices
                count += 1
                count += submatrix_with_n_numbers(matrix[i+1:], n)
    
    return count
