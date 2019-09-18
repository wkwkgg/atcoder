N, X = map(int, input().split())
L = list(map(int, input().split()))

d, res = 0, 1
for l in L:
    d += l
    if d <= X:
        res += 1
    else:
        break
print(res)
