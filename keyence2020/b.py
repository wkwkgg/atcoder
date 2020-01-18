N = int(input())

Sn, Tn = [0] * N, [0] * N
XLn = []
for i in range(N):
    x, l = map(int, input().split())
    Sn[i], Tn[i] = x-l, x+l

for i in range(N):
    XLn.append((Tn[i], Sn[i]))

XLn = sorted(XLn, key=lambda x: x[0])

XLn = sorted(XLn, key=lambda x: x[0])
res, t = 0, -float("inf")
for i in range(N):
    if t <= XLn[i][1]:
        res += 1
        t = XLn[i][0]

print(res)
