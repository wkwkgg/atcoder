N = int(input())
K = int(input())
x = list(map(int, input().split()))

m = K / 2
ans = 0
for i in range(N):
    if x[i] < m:
        ans += 2 * x[i]
    else:
        ans += 2 * (K - x[i])
print(ans)