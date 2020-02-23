def pow_k(x, n):
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n % 2 != 0:
            K = K * x
            x = x ** 2
            n = (n - 1) // 2
        else:
            x = x ** 2
            n = n // 2

    return K * x


MOD = 10**9 + 7

N = int(input())
An = list(map(int, input().split()))

res = 0
for d in range(60):
    n0, n1 = 0, 0
    for i in range(N):
        if (An[i] >> d) & 1:
            n1 += 1
        else:
            n0 += 1

    temp = pow_k(2, d) % MOD
    temp *= (n0*n1) % MOD
    res = (res + temp) % MOD

print(res)
