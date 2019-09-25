from collections import Counter

N = int(input())
A = [int(input()) for _ in range(N)]

cnt = Counter(A)
ans = 0
for num, val in cnt.items():
    if val % 2 != 0:
        ans += 1
print(ans)
