N, M = map(int, input().split())
Xm = list(map(int, input().split()))

ans = 0
if N < M:
    Xm = sorted(Xm)
    Ym = [0] * (M-1)

    for i in range(1, M):
        Ym[i-1] = abs(Xm[i] - Xm[i-1])

    Ym = sorted(Ym, reverse=True)
    for i in range(N-1):
        Ym[i] = 0

    ans = sum(Ym)

print(ans)
