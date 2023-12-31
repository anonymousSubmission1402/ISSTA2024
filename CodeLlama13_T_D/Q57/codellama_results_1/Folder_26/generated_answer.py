
def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sum_of_submatrix = np.sum(matrix[i:k+1, j:l+1])
                    if sum_of_submatrix == 997:
                        submatrices.append((i, j, k, l))
    return submatrices
