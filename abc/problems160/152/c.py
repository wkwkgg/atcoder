N = int(input())
Pn = list(map(int, input().split()))

MIn, MAn = [float("inf")] * N, [-float("inf")] * N
mi, ma = float("inf"), -float("inf")
for i in range(N):
    mi = min(mi, Pn[i])
    ma = max(ma, Pn[i])

    MIn[i], MAn[i] = mi, ma

ans = 1
for i in range(N):
    if Pn[i] == MIn[i] and Pn[i] < MAn[i]:
        ans += 1

print(ans)
