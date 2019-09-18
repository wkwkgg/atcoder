from math import sqrt
N = int(input())

ans = float("inf")
for i in range(1, int(sqrt(N)+1)):
    for j in range(i, N//i + 1):
        ans = min(ans, (j-i)+(N-i*j))
print(ans)
