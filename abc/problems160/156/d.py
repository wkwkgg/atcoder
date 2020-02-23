N, A, B = map(int, input().split())
MOD = 10**9 + 7


# nCa % MOD を X/Y % MOD とおいたときの X,Y を求めるやつ
def f(n, a):
    x, y = 1, 1
    for i in range(1, a + 1):
        x = x * (n - i + 1) % MOD
        y = y * i % MOD
    return x, y


def modpow(a: int, p: int, mod: int) -> int:
    res = 1
    while p > 0:
        if p & 1 > 0:
            res = res * a % mod
        a = a**2 % mod
        p >>= 1
    return res


# a,b の制約なしの解
ans = modpow(2, N, MOD) - 1
a_x, a_y = f(N, A)
b_x, b_y = f(N, B)

a = a_x * modpow(a_y, (MOD - 2), MOD) % MOD
b = b_x * modpow(b_y, (MOD - 2), MOD) % MOD
print((ans - a - b) % MOD)
