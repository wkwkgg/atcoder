N, M, X = map(int, input().split())
A = list(map(int, input().split()))

right = 0
for i in range(X, N+1):
    if i in A:
        right += 1

left = 0
for i in range(0, X)[::-1]:
    if i in A:
        left += 1

print(min(left, right))