W, H, N = map(int, input().split())
xya = [list(map(int, input().split())) for _ in range(N)]

p1, p2 = [0, 0], [W, H]

for *p, a in xya:
    if a == 1:
        if p1[0] < p[0]:
            p1[0] = p[0]
    elif a == 2:
        if p2[0] > p[0]:
            p2[0] = p[0]
    elif a == 3:
        if p1[1] < p[1]:
            p1[1] = p[1]
    else:
        if p2[1] > p[1]:
            p2[1] = p[1]

if p2[0]-p1[0] < 0 or p2[1] - p1[1] < 0:
    print(0)
else:
    print((p2[0]-p1[0]) * (p2[1] - p1[1]))