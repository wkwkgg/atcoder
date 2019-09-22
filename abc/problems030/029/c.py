import sys
sys.setrecursionlimit(10**6)

N = int(input())
ss = list("abc")

ans = []
def dfs(s: str):
    if len(s) == N:
        ans.append(s)
        return

    for a in ss:
        dfs(s + a)

for a in ss:
    dfs(a)

print("\n".join(ans))
