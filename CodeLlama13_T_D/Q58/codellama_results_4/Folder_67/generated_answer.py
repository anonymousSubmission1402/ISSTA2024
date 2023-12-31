
import numpy as np

def submatrix_with_n_numbers(mat, n):
    rows = mat.shape[0]
    cols = mat.shape[1]
    
    count = 0
    for i in range(rows-n+1):
        for j in range(cols-n+1):
            submatrix = mat[i:i+n,j:j+n]
            if np.count_nonzero(submatrix == n) == n**2:
                count += 1
    
    return count
