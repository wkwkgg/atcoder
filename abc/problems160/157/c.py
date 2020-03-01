from collections import defaultdict
N, M = map(int, input().split())
sc = defaultdict(list)

for i in range(M):
    s, c = map(int, input().split())
    sc[s].append(c)

ans = [-1] * N
res = True
for s, c in sc.items():
    if len(set(c)) != 1:
        res = False
        break
    else:
        ans[s - 1] = c[0]

if N == 1 and ans[0] == -1:
    ans[0] = 0
elif N > 1 and ans[0] == 0:
    res = False
else:
    if ans[0] == -1:
        ans[0] = 1

    for i in range(1, N):
        if ans[i] == -1:
            ans[i] = 0

print("".join(list(map(str, ans))) if res else "-1")
