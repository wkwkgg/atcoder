from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

d = defaultdict(int)
d2 = defaultdict(int)
for k in S:
    d[k] += 1
    d2[k] = 0

for k in d2:
    d2[k] = S.count(k) - T.count(k)

d2 = sorted(d2.items(), key=lambda x: x[1], reverse=True)

print(d2[0][1] if d2[0][1] >= 0 else 0)