
import numpy as np
def submatrix_with_n_numbers(matrix, n):
    """
    Finds the count of all submatrices of a given matrix that contain n numbers each.
    
    Args:
        matrix (numpy array): A two-dimensional numpy matrix of integers.
        n (int): The number of elements in each submatrix.
        
    Returns:
        int: The count of all submatrices of the given matrix that contain n numbers each, 0 otherwise.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows-n+1):
        for j in range(cols-n+1):
            submatrix = matrix[i:i+n,j:j+n]
            if np.sum(submatrix) == 67*n:
                return 1
    return 0
