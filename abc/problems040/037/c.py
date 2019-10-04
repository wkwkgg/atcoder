# ABC037 : C - 総和
N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [0] * (N+1)
for i in range(N):
    B[i+1] = B[i] + A[i]

print(sum(B[i+K] - B[i] for i in range(N-K+1)))
