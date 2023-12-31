
import numpy as np

def submatrix_with_particular_sum(mat):
    n = mat.shape[0]
    m = mat.shape[1]
    
    for i in range(n-1):
        for j in range(m-1):
            sum = 0
            for k in range(i, n):
                for l in range(j, m):
                    sum += mat[k][l]
                    if sum == -50:
                        return [mat[i:k+1, j:l+1]]
    
    return []
