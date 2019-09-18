H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

dx = [1, 0, -1, 0, 1, -1, -1, 1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

for h in range(H):
    for w in range(W):
        if S[h][w] == "#": 
            continue
        num = 0
        for d in range(8):
            hd, wd = h + dy[d], w + dx[d]

            if hd < 0 or H <= hd: continue
            if wd < 0 or W <= wd: continue
            if S[hd][wd] == "#": num += 1
        S[h][w] = str(num)

for h in range(H):
    print("".join(S[h]))
