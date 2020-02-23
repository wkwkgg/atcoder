X = int(input())

ans = 1
if X > 6 and X <= 11:
    ans = 2
elif X > 11:
    p, q = divmod(X, 11)
    ans = p*2
    if q > 0 and q <= 6:
        ans += 1
    if q > 6 and q <= 10:
        ans += 2

print(ans)
