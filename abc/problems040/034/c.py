MOD = 10**9 + 7
H, W = map(int, input().split())

a = 1
for i in range(2, H+W-1):
    a = a * i % MOD
b = 1
for i in range(2, H):
    b = b * i % MOD
c = 1
for i in range(2, W):
    c = c * i % MOD

print(a * pow(b*c, MOD-2, MOD) % MOD)
