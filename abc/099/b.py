def h(k):
    return (1 + k)*k // 2

a, b = map(int, input().split())

ans = 1
for i in range(1, 999):
    x = h(i) - a
    y = h(i+1) - b
    if x == y:
        ans = x
        break
print(ans)