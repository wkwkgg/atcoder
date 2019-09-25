import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

bl = [bisect.bisect_left(A, b) for b in B]
for i in range(1, N):
    bl[i] += bl[i-1]
cl = [bisect.bisect_left(B, c) for c in C]

ans = 0
for c in cl:
    if c < 1:
        continue
    ans += bl[c-1]
print(ans)
