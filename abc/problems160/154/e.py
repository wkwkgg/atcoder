from itertools import product

N = int(input())
K = int(input())

ans = 0
for res in product(range(0, 10), repeat=3):
    i = 100*res[0] + 10*res[1] + res[2]
    if i >= K:
        break
    ans += 1

print(ans)
