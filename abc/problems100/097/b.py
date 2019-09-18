from math import sqrt
X = int(input())
ans = 1
for i in range(2, int(sqrt(X))+1):
    j = 2
    while i**j <= X:
        ans = max(ans, i**j)
        j += 1
print(ans)
