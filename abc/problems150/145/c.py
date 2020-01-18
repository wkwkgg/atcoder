from itertools import permutations
from math import factorial


def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


N = int(input())

xs, ys = [], []
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

res = 0
for perm in permutations(range(N), N):
    for i, j in zip(perm[:N-1], perm[1:]):
        res += distance(xs[i], ys[i], xs[j], ys[j])

print(res/factorial(N))
