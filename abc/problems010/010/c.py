def f(x, y):
    r1 = ((x - TXa)**2 + (y - TYa)**2)**0.5
    r2 = ((TXb - x)**2 + (y - TYb)**2)**0.5
    return r1 + r2


TXa, TYa, TXb, TYb, T, V = map(int, input().split())
N = int(input())

temp = 10**9
for _ in range(N):
    x, y = map(int, input().split())
    temp = min(temp, f(x, y))

print("YES" if T*V >= temp else "NO")
