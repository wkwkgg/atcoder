A, B, X = map(int, input().split())

low, high = 1, 10**9
res = 0
while low <= high:
    N = (low + high) // 2

    p = A*N + B*len(str(N))
    if p == X:
        res = N
        break

    if p > X:
        high = N - 1
    else:
        res = N
        low = N + 1

print(res)
