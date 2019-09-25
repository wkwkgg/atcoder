N, M = map(int, input().split())

ans = 0
if N != 1 and M != 1:
    ans = (N-2) * (M-2)
elif N == 1 and M != 1:
    ans = N * (M-2)
elif N != 1 and M == 1:
    ans = (N-2) * M
else:
    ans = 1
print(ans)
