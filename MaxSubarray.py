import sys
import math
input = sys.stdin.readline

# Mostly same code as lecture notes, added another base case,
# also fixed what I assume was a typo in line 16, A[mid-1]
# rather than just adding the index.

def find_max(A, n):
    if n == 0:
        return -sys.maxsize
    if n == 1:
        return A[0]
    mid = math.floor(n/2)
    B = A[0:mid-1]
    C = A[mid:n]
    return max(find_max(B,len(B)),find_max(C,len(C)),
               MaxLeft(A,mid) + MaxRight(A,mid) + A[mid-1])

def MaxLeft(A,mid):
    best = 0
    sum = 0
    # Different indexing for slicing and regular indexes, shift left
    i = mid - 2
    while i>=0:
        sum = sum + A[i]
        best = max(best, sum)
        i = i - 1
    return best

def MaxRight(A,mid):
    best = 0
    sum = 0
    # Different indexing for slicing and regular indexes, shift left
    i = mid
    while i<=len(A)-1:
        sum = sum + A[i]
        best = max(best, sum)
        i = i + 1
    return best

for _ in range(int(input())):
    n = int(input())
    A = [int(i) for i in input().split()]
    print(find_max(A, n))

# To run this code, type `python3 max_subarray.py < input.txt > output.txt` into the command line.
# To run it with small test cases that you type in by hand, simply run `python3 max_subarray.py`
# from the command line.
# Note that this code is written assuming you are using python 3. It may not work in python 2.