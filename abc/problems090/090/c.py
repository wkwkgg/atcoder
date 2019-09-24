N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]

memo = [[-1] * N for _ in range(2)]
memo[0][0] = A[0][0]
for i in range(2):
    for j in range(N):
        if i == 0:
            if j == 0:
                continue
            memo[i][j] = memo[i][j-1] + A[i][j]
        else:
            if j == 0:
                memo[i][j] = memo[i-1][j] + A[i][j]
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1]) + A[i][j]

print(memo[1][N-1])
