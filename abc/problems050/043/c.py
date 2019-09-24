def f(x, y):
    return (x - y)**2


N = int(input())
A = list(map(int, input().split()))

ans = 10**9
for k in range(-100, 101):
    temp = sum([f(x, k) for x in A])
    ans = min(ans, temp)
print(ans)
