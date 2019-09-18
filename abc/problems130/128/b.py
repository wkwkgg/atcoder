from collections import defaultdict
from operator import itemgetter
N = int(input())

d = defaultdict(list)
for i in range(1,N+1):
    s, p = input().split()
    d[s].append((i, int(p)))

for k,vs in sorted(d.items(), key=itemgetter(0)):
    for i,p in sorted(vs, key=itemgetter(1), reverse=True):
        print(i)