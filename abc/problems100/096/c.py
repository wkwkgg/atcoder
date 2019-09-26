H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            continue

        flag = False
        for dx, dy in d:
            i2, j2 = i+dx, j+dy
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue

            if S[i2][j2] == "#":
                flag = True

        if not flag:
            print("No")
            exit()
print("Yes")
