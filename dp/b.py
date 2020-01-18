# Educational DP Contest : B - Frog 2

N, K = map(int, input().split())
h = list(map(int, input().split())) + [float("inf")] * (K-1)

dp = [0] * N + [float("inf")] * K
for i in range(N-1)[::-1]:
    temp = float("inf")
    for k in range(1, K+1):
        temp = min(temp, abs(h[i+k] - h[i]) + dp[i+k])
    dp[i] = temp

print(dp[0])
