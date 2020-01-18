from itertools import combinations

N = int(input())
dn = list(map(int, input().split()))

print(sum(x*y for x, y in combinations(dn, 2)))
