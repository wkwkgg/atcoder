# C - Good Sequence
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
ans = 0
for num, amount in c.items():
    if num == amount:
        continue
    elif num < amount:
        ans += amount - num
    else:
        ans += amount

print(ans)
