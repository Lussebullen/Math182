import numpy as np


def optimalParanthesization(R, C):
    n = len(R)                  # amount of matrices
    para = [0] * n
    memo = -np.ones((n, n))     # Let -1 denote empty
    for _ in range(n):          # Base case
        memo[_][_] = 0
    return HelperParan(0, n-1, R, C, memo, para)


def HelperParan(i, j, R, C, memo, para):
    if memo[i][j] != -1:
        return memo[i][j]
    memo[i][j] = min([HelperParan(i,k,R,C,memo,para) +
                      HelperParan(k+1, j, R,C,memo,para) +
                      R[i]*C[k]*C[j] for k in range(i,j)])
    return memo[i][j]


print(optimalParanthesization([4,5,2,3], [5,2,3,6]))
