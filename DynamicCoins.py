import math

def DynCoin(V,p):
    memo = [100000] * (p+1)
    memo[0] = 0
    for i in range(0,p+1):
        for v in V:
            if i - v >= 0 and memo[i - v] + 1 < memo[i]:
                memo[i] = memo[i - v] + 1
    return memo[p]



V=[1,2,5]
p=11
print(DynCoin(V,p))