from itertools import combinations

N = int(input())
A = list(map(int, input().split()))

res = 0
for p, q in combinations(A,2):
    res = max(res, abs(p-q))
print(res)