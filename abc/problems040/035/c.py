N, Q = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(Q)]

xs = [0] * (N+1)
for l, r in LR:
    xs[l-1] += 1
    xs[r] -= 1

s = 0
ans = ""
for i in range(N):
    s += xs[i]
    ans += "0" if s % 2 == 0 else "1"

print(ans)
