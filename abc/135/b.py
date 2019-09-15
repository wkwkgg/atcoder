N = int(input())
P = list(map(int, input().split()))
Q = sorted(P)

count = 0
for i in range(N):
    if P[i] != Q[i]:
        count += 1

print("YES" if count <= 2 else "NO")