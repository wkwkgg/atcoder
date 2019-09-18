N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    if X >> i & 1:
        ans += A[i]
print(ans)