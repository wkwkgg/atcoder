N = int(input())
W = list(map(int, input().split()))

s1, s2 = sum(W), 0
res = abs(s1 - s2)
for w in W:
    s1 -= w
    s2 += w
    res = min(res, abs(s1 - s2))
print(res)