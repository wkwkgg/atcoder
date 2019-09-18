from itertools import permutations
A = list(map(int, input().split()))

res = float("inf")
for a,b,c in permutations(A):
    res = min(res, abs(a-b) + abs(b-c))
print(res)