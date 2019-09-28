from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

c = Counter(A)
ans = 0
size = len(c.keys())

if size > K:
    temp = size - K
    ans += sum(v for _, v in sorted(c.items(), key=lambda x: x[1])[:temp])

print(ans)
