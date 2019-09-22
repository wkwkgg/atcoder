N = int(input())
V = sorted(list(map(int, input().split())))

for i in range(1, N):
    V[i] = (V[i-1] + V[i]) / 2
print(V[N-1])
