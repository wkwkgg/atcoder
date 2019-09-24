from collections import Counter

N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

cnt = Counter(A)

ans = [0] * N
for i in range(N):
    ans[i] = K + cnt[i+1] - Q

print("\n".join("Yes" if val > 0 else "No" for val in ans))
