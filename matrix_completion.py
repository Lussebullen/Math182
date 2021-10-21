import sys
input = sys.stdin.readline
from heapq import *

# Hint: look up python's `heapq` class for an efficient implementation of a binary heap (which you may use without implementing a heap yourself)

def complete_matrix(n, R, C, M):
    #Immediately discard:
    if sum(R) != sum(C):
        return False

    #Attempt solution
    Q = []
    for _ in range(n):
        heappush(Q,(-C[_],_))

    for _ in range(n):
        repush = []
        for k in range(R[_]):
            prio = heappop(Q)
            M[_][prio[1]] = 1
            #Save entries popped with decremented value
            repush = repush + [(prio[0] + 1, prio[1])]
        #Push decremented values
        for i in repush:
            heappush(Q,i)

    #Check solution
    rsum = [sum(row) for row in M]
    csum = [sum(row[i] for row in M) for i in range(n)]
    if rsum==R and csum==C:
        return True
    else:
        return False

# Change this to a correct solution. It should return a boolean indicating whether it is possible to fill in M given the constraints. If it is possible, it should also set the values in M to some valid solution. You can set the value of the item in row i and position j of M using M[i][j]. Note that M is 0-indexed.

for _ in range(int(input())):
    n = int(input())
    R = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    M = [[0]*n for _ in range(n)]
    possible = complete_matrix(n, R, C, M)
    if possible:
        print("possible")
        for i in range(n):
            print(" ".join(map(str, M[i])))
    else:
        print("impossible")


# To run this code, type `python3 matrix_completion.py < input.txt > output.txt`
# into the command line. To run it with small test cases that you type in by
# hand, simply run `python3 matrix_completion.py` from the command line.
