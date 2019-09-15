N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]
m = min(M)

print(len(M) + (X - sum(M))//m)