import sys
import math
input = sys.stdin.readline

# Mostly same code as lecture notes, added another base case,
# also fixed what I assume was a typo in line 16, A[mid-1]
# rather than just adding the index.

# Ensures 0 is returned for empty initial array, else call the recursive method.
def find_max(A,n):
    if len(A)==0:
        return 0
    else:
        return maxSubArray(A,n)

def maxSubArray(A, n):
    if n == 0:
        # Avoids 0 being the max for empty lists, as this would dominate negative
        # results in the max(...) function in the return statement.
        #return -sys.maxsize

        #Since seemingly 0 is desired I use base case =0
        return 0
    if n == 1:
        return A[0]
    mid = math.floor(n/2)
    B = A[0:mid-1]
    C = A[mid:n]
    return max(maxSubArray(B,len(B)),maxSubArray(C,len(C)),
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


# To run this code, type `python3 MaxSubarray.py < input.txt > output.txt` into the command line.
# To run it with small test cases that you type in by hand, simply run `python3 max_subarray.py`
# from the command line.
# Note that this code is written assuming you are using python 3. It may not work in python 2.