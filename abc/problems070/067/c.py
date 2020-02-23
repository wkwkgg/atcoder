N = int(input())
An = list(map(int, input().split()))

Sn = [0] * (N+1)
for i in range(1, N+1):
    Sn[i] = An[i-1] + Sn[i-1]

ans = float("inf")
for i in range(1, N):
    ans = min(ans, abs(Sn[N]-Sn[i] - Sn[i]))

print(ans)
