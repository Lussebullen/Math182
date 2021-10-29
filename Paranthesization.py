import numpy as np
import math
import sys
input = sys.stdin.readline


def parastring(split):
    n=len(split)
    mult = ["A", "x"] * (n - 1) + ["A"]
    return stringhelper(split,mult,0,n-1,split[0][n-1])


def stringhelper(split,mult,i,j,k):
    if i==j:
        return mult
    splitindex = k * 2
    mult[2 * i] = "(" + mult[2 * i]
    mult[splitindex] = mult[splitindex] + ")"
    mult[splitindex + 2] = "(" + mult[splitindex + 2]
    mult[j * 2] = mult[j * 2] + ")"
    stringhelper(split,mult,i,k,split[i][k])
    stringhelper(split,mult,k+1,j,split[k+1][j])
    for i in range(n):
        while mult[2 * i][0] == "(" and mult[2 * i][-1] == ")":
            mult[2 * i] = mult[2 * i][1: -1]
    return mult

def parenthesize(n,N,M):
    C = [[0]*n for k in range(n)]
    bestSplit = [[0]*n for k in range(n)]
    for l in range(1,n):
        for i in range(0,n-l):
            j = i + l
            val = math.inf
            for k in range(i,j):
                if C[i][k]+C[k+1][j]+N[i]*M[k]*M[j] < val:
                    val = C[i][k]+C[k+1][j]+N[i]*M[k]*M[j]
                    bestSplit[i][j] = k
                C[i][j] = val
    return C[0][n-1], parastring(bestSplit)



for _ in range(int(input())):
    n = int(input())
    N = [int(i) for i in input().split()]
    M = [int(i) for i in input().split()]
    optimal, s = parenthesize(n, N, M)
    print(optimal)
    print("".join(s))

# To run this code, type `python3 chain_matrix.py < input.txt > output.txt`
# into the command line. To run it with small test cases that you type in by
# hand, simply run `python3 chain_matrix.py` from the command line.



########### OLD CODE ############
#
# def parenthesize(n, R, C):
# #    n = len(R)                  # amount of matrices
#     para = ["A","x"] * (n - 1) + ["A"]
#     memo = -np.ones((n, n))     # Let -1 denote empty
#     for _ in range(n):          # Base case
#         memo[_][_] = 0
#     val, para = HelperParan(0, n-1, R, C, memo, para)
#     for i in range(n):
#         while para[2 * i][0] == "(" and para[2 * i][-1] == ")":
#             para[2 * i] = para[2 * i][1: -1]
#     return [val,para]
#
# # Helper function using min - Have to avoid min to determine which distinct case is min.
# #def HelperParan(i, j, R, C, memo, para):
# #    if memo[i][j] != -1:
# #        return memo[i][j]
# #    memo[i][j] = min([HelperParan(i,k,R,C,memo,para) +
# #                      HelperParan(k+1, j, R,C,memo,para) +
# #                      R[i]*C[k]*C[j] for k in range(i,j)])
# #    return memo[i][j]
#
# def HelperParan(i, j, R, C, memo, para):
#     if memo[i][j] != -1:
#         return [memo[i][j],para]
#     best = math.inf
#     bestSplit = - 1
#     for k in range(i,j):
#         val = HelperParan(i,k,R,C,memo,para)[0] + HelperParan(k+1, j, R,C,memo,para)[0] + R[i]*C[k]*C[j]
#         if val < best:
#             bestSplit = k
#             best = val
#     memo[i][j] = best
#
#     # Add parentheses:
#     splitindex = bestSplit * 2
#     para[2 * i] = "(" + para[2 * i]
#     para[splitindex] = para[splitindex] + ")"
#     para[splitindex + 2] = "(" + para[splitindex + 2]
#     para[j * 2] = para[j * 2] + ")"
#
#     return [memo[i][j],para]
#
#
# N=[4,5,2,3]
# M=[5,2,3,6]
# n=len(N)
# val, str = parenthesize(n,N,M)
# print(val)
# print(str)