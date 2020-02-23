L, R = map(int, input().split())

ans = 10**9
for i in range(L, min(R, L+2019)+1):
    for j in range(i+1, min(R, L+2019)+1):
        ans = min(ans, (i % 2019) * (j % 2019) % 2019)

print(ans)
