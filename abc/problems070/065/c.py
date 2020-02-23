N, M = map(int, input().split())

MOD = 10**9 + 7
ans = 0
if abs(N-M) < 2:
    A, B = max(N, M), min(N, M)
    res = 1
    if A == B:
        for i in range(1, A+1):
            res = (i**2 % MOD) * res % MOD
        ans = res * 2 % MOD
    else:
        for a in range(1, A+1):
            res = res * a % MOD
        for b in range(1, B+1):
            res = res * b % MOD
        ans = res % MOD

print(ans)
