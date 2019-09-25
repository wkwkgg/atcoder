C = [list(map(int, input().split())) for _ in range(3)]

ans = True
row = C[0]
for i in range(1, 3):
    for j in range(3):
        C[i][j] -= C[0][j]

    if row != C[i] and len(set(C[i])) != 1:
        ans = False

print("Yes" if ans else "No")
