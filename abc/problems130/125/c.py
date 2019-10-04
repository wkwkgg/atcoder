# ABC125 : C - GCD on Blackboard
from fractions import gcd

N = int(input())
A = list(map(int, input().split()))


def gcd2(x, y):
    if not x:
        return y
    if not y:
        return x
    return gcd(x, y)


L, R = [0] * (N+1), [0] * (N+1)
for i in range(1, N+1):
    L[i] = gcd2(L[i-1], A[i-1])
    R[N-i] = gcd2(R[N-i+1], A[N-i])

ans = 0
for i in range(N):
    ans = max(ans, gcd2(L[i], R[i+1]))

print(ans)
