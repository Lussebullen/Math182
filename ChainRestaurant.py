def maxprofit(A,k):
    #Memoized version
    n = len(A)
    memo = [-1] * n
    memo[0] = A[0]
    return helper(n-1,A,k,memo)

def helper(n,A,k,memo):
    if n<0:
        return 0
    if memo[n] != -1:
        return memo[n]
    memo[n] = max(helper(n-k,A,k,memo)+A[n],helper(n-1,A,k,memo))
    return memo[n]

def iterprof(A,k):
    #Iterable version
    n = len(A)
    memo = [-1] * n
    memo[0] = A[0]
    for i in range(1,n):
        if i-k>=0:
            memo[i] = max(memo[i-k] + A[i], memo[i-1])
        else:
            memo[i] = max(A[i], memo[i-1])
    return memo[n-1]

A = [2,6,5,2,7,43,6,7,2]
k=4
print(maxprofit(A,k))
print(iterprof(A,k))