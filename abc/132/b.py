n = int(input())
p = list(map(int, input().split()))

res = 0
for a,b,c in zip(p[:n-1], p[1:n], p[2:]):
    if a > b > c or c > b > a:
        res += 1
print(res)