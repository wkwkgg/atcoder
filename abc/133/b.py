from itertools import combinations
from math import sqrt
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

res = 0
for Y,Z in combinations(X, 2):
    r = sqrt(sum((y-z)**2 for y,z in zip(Y,Z)))
    if r == float(int(r)):
        res += 1
print(res)