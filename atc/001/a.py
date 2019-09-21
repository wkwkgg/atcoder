import sys
sys.setrecursionlimit(10 ** 6)

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
reached = [[False] * W for _ in range(H)]

s, g = None, None
for i in range(H):
    if 's' in C[i]: s = (i, C[i].index('s'))
    if 'g' in C[i]: g = (i, C[i].index('g'))

def search(x, y):
    if x < 0 or H <= x or y < 0 or W <= y:
        return
    if C[x][y] == "#":
        return
    if reached[x][y]:
        return

    reached[x][y] = True
    search(x+1, y)
    search(x-1, y)
    search(x, y+1)
    search(x, y-1)

search(*s)
print("Yes" if reached[g[0]][g[1]] else "No")
