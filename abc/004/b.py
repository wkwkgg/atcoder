N = 4
C = [input().split() for _ in range(N)]
D = [[""] * N for _ in range(N)]
ans = ""
for i in range(N):
    for j in range(N):
        D[i][j] = C[N-i-1][N-j-1]
    ans += " ".join(D[i]) + "\n"
print(ans, end="")
