N, Y = map(int, input().split())

x, y, z = 10000, 5000, 1000
for i in range(N+1):
    for j in range(N-i+1):
        k = N-i-j
        if (x*i + y*j) == (Y - z*k):
            print(i, j, k)
            exit()
print("-1 -1 -1")