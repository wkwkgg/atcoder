MAX = 10**9

N = int(input())
T = [int(input()) for _ in range(N)]

ans = MAX
for i in range(2**N):
    left, right = [], []
    for j in range(N):
        if i >> j & 1:
            left.append(N - 1 - j)
        else:
            right.append(N - 1 - j)
    temp = max(sum(T[k] for k in left), sum(T[k] for k in right))
    ans = min(ans, temp)

print(ans)