from math import sqrt

N = int(input().rstrip())

ans = "YES"
for i in range(2, int(sqrt(N))+1):
    if N % i == 0:
        ans = "NO"
        break

print(ans)
