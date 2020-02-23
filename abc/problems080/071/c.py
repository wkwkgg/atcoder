# C - Make a Rectangle
from collections import defaultdict

N = int(input())
An = list(map(int, input().split()))

d = defaultdict(int)
for i in range(N):
    d[An[i]] += 1

edges = sorted(d.items(), key=lambda x: x[0], reverse=True)
w, h = 0, 0
ans = 0
for edge, amount in edges:
    if amount < 2:
        continue

    if amount >= 4:
        w, h = max(w, edge), max(h, edge)
        ans = max(ans, w*h)
    if amount >= 2:
        if not w:
            w = edge
        else:
            h = edge
            ans = max(ans, w*h)

print(ans)
