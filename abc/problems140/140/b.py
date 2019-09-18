N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

res = sum(B)
for i, (p, n) in enumerate(zip(A[:N-1], A[1:])):
    if n - p == 1:
        res += C[A[i]-1]
print(res)