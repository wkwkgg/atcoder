from collections import defaultdict
N = int(input())
d = defaultdict(int)
for _ in range(N):
    d[input()] += 1

print(sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0])