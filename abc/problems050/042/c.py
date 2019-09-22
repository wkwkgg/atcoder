import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
D = set(map(int, input().split()))

INF = 10**9
ans = INF
def dfs(price):
    if price > 10*N: return INF

    if not D & set(map(int, list(str(price)))):
        return price

    return dfs(price + 1)

ans = min(ans, dfs(N))
print(ans)
