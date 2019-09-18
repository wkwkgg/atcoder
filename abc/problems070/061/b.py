N, M = map(int, input().split())

g = [[0] * (N+1) for _ in range(N+1)]

for m in range(M):
    a, b = map(int, input().split())
    g[a][b] += 1
    g[b][a] += 1

for i in range(1, N+1):
    print(sum(g[i]))
