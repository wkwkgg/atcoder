from itertools import combinations

N = int(input())
Sn = [input() for _ in range(N)]

march = ["M", "A", "R", "C", "H"]
d = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
cnt = 0
for i in range(N):
    if Sn[i][0] not in march:
        continue
    d[Sn[i][0]] += 1
    cnt += 1

ans = 0
for a, b, c in combinations(march, 3):
    ans += d[a] * d[b] * d[c]

print(ans)
