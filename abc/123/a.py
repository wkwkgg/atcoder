from itertools import combinations

xs = [int(input()) for _ in range(5)]
k = int(input())

res = True
for a, b in combinations(xs, 2):
    if abs(a - b) > k:
        res = False
        break
print("Yay!" if res else ":(")