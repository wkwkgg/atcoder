# ABC028 : C - 数を3つ選ぶマン

from itertools import combinations
ins = list(map(int, input().split()))

res = []
for xs in combinations(ins, 3):
    res.append(sum(xs))

print(sorted(res, reverse=True)[2])
