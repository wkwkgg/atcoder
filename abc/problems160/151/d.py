from collections import deque
from itertools import product

H, W = map(int, input().split())
Shw = [list(input()) for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    que = deque()
    res = 0
    dist = [[-1 for _ in range(W)] for _ in range(H)]

    que.append((x, y))
    dist[x][y] = 0
    while que:
        x, y = que.pop()
        res = max(res, dist[x][y])

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if Shw[nx][ny] == "#":
                continue

            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                que.appendleft((nx, ny))
    return res


ans = 0
for x, y in product(range(H), range(W)):
    if Shw[x][y] == "#":
        continue
    ans = max(ans, bfs(x, y))
print(ans)
