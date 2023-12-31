
import numpy as np

def submatrix_with_n_numbers(arr):
    n = 24
    rows, cols = arr.shape
    count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            if np.all(arr[i:i+n,j:j+n] == n):
                count += 1
    return count
