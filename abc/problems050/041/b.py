A, B, C = map(int, input().split())
MOD = 10**9 + 7

ab = A * B % MOD
abc = ab * C % MOD
print(abc)