# C - Grand Garden

N = int(input())
H = list(map(int, input().split()))

ans, cur = 0, 0
for h in H:
    if cur < h:
        ans += h - cur
    cur = h
print(ans)
