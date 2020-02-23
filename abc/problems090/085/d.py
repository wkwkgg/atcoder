from math import ceil

N, H = map(int, input().split())
An, Bn = [0] * N, [0] * N
for i in range(N):
    An[i], Bn[i] = map(int, input().split())

ans = 0
a_max = max(An)
for b in sorted(Bn, reverse=True):
    if b < a_max:
        break
    H -= b
    ans += 1
    if H <= 0:
        break

if H > 0:
    ans += ceil(H/a_max)

print(ans)
