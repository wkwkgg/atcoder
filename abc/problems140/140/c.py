N = int(input())
B = list(map(int, input().split()))

A = [B[0]] + [0] * (N-2) + [B[-1]]
for i, (prv, nxt) in enumerate(zip(B[:-1], B[1:]), 1):
    A[i] = min(prv, nxt)
print(sum(A))
