N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = N + X
for n in range(N):
    ans += len(list(filter(lambda x: x <= D, [i*A[n] + 1 for i in range(1, D+1)])))
print(ans)
