N = int(input())
A = list(map(int, input().split()))
xs = []
for i in range(N):
    xs.append((i+1, A[i]))

xs = sorted(xs, key=lambda x: x[1])

print(" ".join(str(x[0]) for x in xs))
