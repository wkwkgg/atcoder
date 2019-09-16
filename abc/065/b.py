N = int(input())
g = [1] + [0] * (N-1)
map = [(i, int(input())-1) for i in range(N)]

ans = 0
current = 0
while g[1] != 1:
    dst = map[current][1]
    if g[dst] == 1:
        ans = -1
        break
    ans += 1
    current = dst
    g[dst] = 1
print(ans)