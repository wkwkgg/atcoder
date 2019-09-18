N = int(input())
A = list(map(int, input().split()))

if sum(A)%N != 0:
    ans = -1
else:
    ans = 0
    n = sum(A) // N
    for i in range(1, N):
        s = sum(A[:i])
        if i*n != s:
            ans += 1
print(ans)