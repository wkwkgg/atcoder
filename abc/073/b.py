N = int(input())
lr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for l, r in lr:
    ans += (r - l) + 1
print(ans)
