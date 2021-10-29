import numpy as np
import math
import sys
#input = sys.stdin.readline

def parenthesize(n, R, C):
#    n = len(R)                  # amount of matrices
    para = ["A","x"] * (n - 1) + ["A"]
    memo = -np.ones((n, n))     # Let -1 denote empty
    for _ in range(n):          # Base case
        memo[_][_] = 0
    val, para = HelperParan(0, n-1, R, C, memo, para)
    for i in range(n):
        while para[2 * i][0] == "(" and para[2 * i][-1] == ")":
            para[2 * i] = para[2 * i][1: -1]
    return [val,para]

# Helper function using min - Have to avoid min to determine which distinct case is min.
#def HelperParan(i, j, R, C, memo, para):
#    if memo[i][j] != -1:
#        return memo[i][j]
#    memo[i][j] = min([HelperParan(i,k,R,C,memo,para) +
#                      HelperParan(k+1, j, R,C,memo,para) +
#                      R[i]*C[k]*C[j] for k in range(i,j)])
#    return memo[i][j]

def HelperParan(i, j, R, C, memo, para):
    if memo[i][j] != -1:
        return [memo[i][j],para]
    best = math.inf
    bestSplit = - 1
    for k in range(i,j):
        val = HelperParan(i,k,R,C,memo,para)[0] + HelperParan(k+1, j, R,C,memo,para)[0] + R[i]*C[k]*C[j]
        if val < best:
            bestSplit = k
            best = val
    memo[i][j] = best

    # Add parentheses:
    splitindex = bestSplit * 2
    para[2 * i] = "(" + para[2 * i]
    para[splitindex] = para[splitindex] + ")"
    para[splitindex + 2] = "(" + para[splitindex + 2]
    para[j * 2] = para[j * 2] + ")"

    return [memo[i][j],para]

print(parenthesize(10,[7, 48, 100, 52, 64, 58, 55, 32, 31, 33], [48, 100, 52, 64, 58, 55, 32, 31, 33, 38]))


#for _ in range(int(input())):
#    n = int(input())
#    N = [int(i) for i in input().split()]
#    M = [int(i) for i in input().split()]
#    optimal, s = parenthesize(n, N, M)
#    print(optimal)
#    print("".join(s))

# To run this code, type `python3 chain_matrix.py < input.txt > output.txt`
# into the command line. To run it with small test cases that you type in by
# hand, simply run `python3 chain_matrix.py` from the command line.