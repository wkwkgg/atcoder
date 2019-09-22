N = int(input())
H = list(map(int, input().split()))

memo = [0] * N
for i in range(N-1)[::-1]:
    if H[i] >= H[i+1]:
        memo[i] = memo[i+1] + 1
print(max(memo))