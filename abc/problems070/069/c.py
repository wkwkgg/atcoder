N, M = map(int, input().split())

s, c = N, M // 2

ans = 0
if s > c:
    ans = c
else:
    ans = (M - s*2) // 4 + s
print(ans)
