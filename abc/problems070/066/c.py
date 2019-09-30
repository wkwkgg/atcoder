# C - pushpush
from collections import deque

N = int(input())
A = input().split()

offset = 0 if N % 2 == 0 else 1
ans = deque([A[0]])
for i in range(1, N):
    if (i+offset) % 2 == 0:
        ans.append(A[i])
    else:
        ans.appendleft(A[i])

print(" ".join(ans))
