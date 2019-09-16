N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(M)]

def f(a, b, x, y):
    return abs(a-x) + abs(b-y)

ans = [0] * N
for i, _ab in enumerate(ab):
    temp = float("inf")
    for j, _cd in enumerate(cd):
        dist = f(_ab[0], _ab[1], _cd[0], _cd[1])
        if dist < temp: 
            temp, ans[i] = dist, j + 1

for r in ans:
    print(r)

    