import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    a_transpose = []
    for i in range(len(A[0])):
        tmp = []
        for j in range(len(A)):
            tmp.append(A[j][i])
        a_transpose.append(np.array(tmp))
    return np.array(a_transpose)
