N, K = map(int, input().split())
Hn = list(map(int, input().split()))

ans = 0
Hn = sorted(Hn)
for i in range(N-K):
    ans += Hn[i]

print(ans)
