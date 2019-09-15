N, L = map(int, input().split())
t = [L+i-1 for i in range(1, N+1)]
m = min(map(abs, t))
k = min(t)

res = 0
if m == k:
    res = sum(t) - m
else:
    res = sum(t) + m
print(res)