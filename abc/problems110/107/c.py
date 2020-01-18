N, K = map(int, input().split())
Xn = list(map(int, input().split()))

Ln = [0] * N
for i in range(N-1):
    Ln[i+1] = abs(Xn[i+1] - Xn[i]) + Ln[i]

Rn = [0] * N
for i in range(1, N)[::-1]:
    Rn[i-1] = abs(Xn[i] - Xn[i-1]) + Rn[i]

ans = float("inf")
for i in range(N-K+1):
    ans = min(ans, abs(Xn[i]) + Ln[i+K-1] - Ln[i])

for i in range(K-1, N)[::-1]:
    ans = min(ans, abs(Xn[i]) + Rn[i-K+1] - Rn[i])

print(ans)
