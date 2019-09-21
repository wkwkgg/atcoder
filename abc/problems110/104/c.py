from math import ceil
D, G = map(int, input().split())
p, c = [0] * D, [0] * D
for i in range(D):
    p[i], c[i] = map(int, input().split())

ans = 10**9
for i in range(2**D):
    s, num, rest = 0, 0, -1
    for j in range(D):
        if i >> j & 1:
            s += 100 * (j+1) * p[j] + c[j]
            num += p[j]
        else:
            rest = j
    if s < G:
        s1 = 100 * (rest + 1)
        need = ceil((G - s) / s1)
        if need >= p[rest]:
            continue
        num += need
    ans = min(ans, num)

print(ans)