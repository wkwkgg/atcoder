W, a, b = map(int, input().split())

ans = 0
if a < b:
    if a+W < b:
        ans = abs(b - (a+W))
else:
    if b+W < a:
        ans  = abs(a - (b+W))
print(ans)