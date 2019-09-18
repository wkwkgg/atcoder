N, M, C = map(int, input().split())
blist = list(map(int, input().split()))
alist = [list(map(int, input().split())) for _ in range(N)]

print(sum([1 if sum(t[0]*t[1] for t in zip(alist[i], blist)) + C > 0 else 0 for i in range(N)]))