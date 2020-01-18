# Educational DP Contest : A - Frog 1

N = int(input())
h = list(map(int, input().split())) + [float("inf")]

dp = [0] * N + [float("inf")]
for i in range(N-1)[::-1]:
    dp[i] = min(abs(h[i+1] - h[i]) + dp[i+1],
                abs(h[i+2] - h[i]) + dp[i+2])

print(dp[0])
