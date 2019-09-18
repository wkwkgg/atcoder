from collections import defaultdict
N = int(input())
A = [int(input()) for _ in range(N)]
ans = 0

d = defaultdict(int)
for a in A:
    if d[a] != 0:
        ans += 1
    else:
        d[a] += 1
print(ans)