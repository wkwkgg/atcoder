from collections import defaultdict

N, M = map(int, input().split())
PYm = [0] * M

order = dict()
for i in range(M):
    key = input().strip()
    PYm[i] = list(map(int, key.split()))
    order[key] = i

d = defaultdict(list)
for i in range(M):
    d[PYm[i][0]].append(PYm[i][1])

res = dict()
for pi, ys in d.items():
    for i, y in enumerate(sorted(ys), 1):
        res["{} {}".format(pi, y)] = "{:0>6}{:0>6}".format(pi, i)

for key, _ in sorted(order.items(), key=lambda x: x[1]):
    print(res[key])
