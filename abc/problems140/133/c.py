L, R = map(int, input().split())

ans = 10**9
rng = R - L
if rng > 2019:
    ans = 0
else:
    for i in range(L, R+1):
        for j in range(L, R+1):
            if i != j:
                ans = min(ans, i*j % 2019)

print(ans)
