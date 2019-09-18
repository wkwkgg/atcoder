N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = 0
start, end = A[0], A[0]+T
for i in range(1,len(A)):
    if end > A[i]:
        end = A[i] + T
    else:
        ans += end - start
        start, end = A[i], A[i] + T

ans += end - start
print(ans)