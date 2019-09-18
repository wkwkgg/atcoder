from math import sqrt, ceil

N = int(input())
ans = 0
for n in range(1, N+1, 2):
    count = 0
    for i in range(1, ceil(sqrt(n))+1):
        if n%i == 0:
            count += 2
    if count == 8:
        ans += 1
print(ans)

