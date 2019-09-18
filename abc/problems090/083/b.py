N, A, B = map(int, input().split())
ans = 0
for n in range(N+1):
    s = sum(map(int, list(str(n))))
    if A <= s <= B:
        ans += n
print(ans)