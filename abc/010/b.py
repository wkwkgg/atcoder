N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    r = a%6
    if r in {1,3}:
        ans += 0
    elif r == 0:
        ans += 3
    else:
        ans += 1 if r < 3 else r-3
print(ans)