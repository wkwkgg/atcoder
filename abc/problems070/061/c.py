N, K = map(int, input().split())
ABn = [tuple(map(int, input().split())) for i in range(N)]

ABn = sorted(ABn, key=lambda x: x[0])
crr = K
ans = 0
for i in range(N):
    crr -= ABn[i][1]
    if crr <= 0:
        ans = ABn[i][0]
        break

print(ans)
