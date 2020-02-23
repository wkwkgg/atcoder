N = int(input())
Sn = [int(input()) for _ in range(N)]

ans = sum(Sn)
if ans % 10 == 0:
    Xs, Ys = [], []
    for i in range(N):
        if Sn[i] % 10 == 0:
            Xs.append(Sn[i])
        else:
            Ys.append(Sn[i])

    if len(Ys) != 0:
        m = min(Ys) if len(Ys) > 1 else 0
        ans = sum(Xs) + sum(Ys) - m
    else:
        ans = 0
print(ans)
