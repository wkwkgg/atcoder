N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

for ly in range(N):
    for lx in range(N):
        # 見ている範囲が NxN を超えている
        if ly+M-1 >= N or lx+M-1 >= N: continue

        # NxN を見ている範囲と MxM の match を探索
        match = True
        for y in range(M):
            for x in range(M):
                if A[ly+y][lx+x] != B[y][x]:
                    match = False
        if match:
            print("Yes")
            exit()

print("No")