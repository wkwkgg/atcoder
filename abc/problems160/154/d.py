N, K = map(int, input().split())
Pn = list(map(int, input().split()))


def f(n):
    return (1+n)*n/2


Rn = list(map(lambda x: f(x)/x, Pn))

Sn = [0] * (N+1)
for i in range(1, N+1):
    Sn[i] = Sn[i-1] + Rn[i-1]

ans = -float("inf")
for i in range(K, N+1):
    # print(i, i-1)
    ans = max(ans, Sn[i] - Sn[i-K])

print(ans)
