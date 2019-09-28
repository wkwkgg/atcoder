from collections import Counter

N = int(input())
A = list(map(int, input().split()))
c = Counter(A)

ans = 0
for i in c:
    ans = max(ans, c[i-1] + c[i] + c[i+1])
print(ans)
