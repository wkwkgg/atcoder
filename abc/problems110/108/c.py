N, K = map(int, input().split())

nums = [0] * K
for i in range(1, N + 1):
    nums[i % K] += 1

ans = 0
for i in range(K):
    b = (K - i) % K
    c = (K - i) % K
    if (b + c) % K != 0: continue

    ans += nums[i] * nums[b] * nums[c]

print(ans)
