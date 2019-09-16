A, B, C = map(int, input().split())
ans = "NO"
for i in range(1, 101):
    if (B*i+C)%A == 0:
        ans = "YES"
print(ans)