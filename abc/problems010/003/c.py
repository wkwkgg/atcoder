N, K = map(int, input().split())
R = sorted(list(map(int, input().split())))

rs = R[-K:]
ans = 0
for r in rs:
    ans = (ans + r) / 2

print(ans)
