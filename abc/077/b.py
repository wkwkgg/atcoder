from math import sqrt
N = int(input())
ans = 1
for i in range(2, int(sqrt(N))+1):
    ans = max(ans, i**2)
print(ans)
