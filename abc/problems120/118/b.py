N, M = map(int, input().split())
KA = [list(map(int, input().split())) for _ in range(N)]

res = set(KA[0][1:])
for a in KA[1:]:
    res = res & set(a[1:])
print(len(res))