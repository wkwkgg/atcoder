N = int(input())
S = [list(input()) for _ in range(N)]
ans = [[None] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        ans[i][j] = S[N-1-j][i]

for i in range(N):
    print("".join(ans[i]))