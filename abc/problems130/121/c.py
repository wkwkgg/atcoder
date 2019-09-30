# C - Energy Drink Collector
N, M = map(int, input().split())
d = sorted([list(map(int, input().split())) for _ in range(N)])

ans = 0
for price, amount in d:
    if M <= 0:
        break
    k = amount if amount < M else M
    ans += price * k
    M -= k

print(ans)
