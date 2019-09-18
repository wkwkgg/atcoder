N = int(input())
SP = []
for i in range(N):
    s, p = input().split()
    SP.append((s, int(p)))

m = sum(p for s,p in SP)

ans = "atcoder"
for s,p in SP:
    if p > m/2:
        ans = s
print(ans)