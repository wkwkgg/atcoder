N = int(input())
ans = 0
for _ in range(N):
    x, u = input().split()
    if u == "BTC":
        ans += (380000 * float(x))
    else:
        ans += float(x)
print(ans)