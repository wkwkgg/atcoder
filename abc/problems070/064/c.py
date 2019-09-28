from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
for a in A:
    if a < 400:
        d[0] += 1
    elif 400 <= a < 800:
        d[1] += 1
    elif 800 <= a < 1200:
        d[2] += 1
    elif 1200 <= a < 1600:
        d[3] += 1
    elif 1600 <= a < 2000:
        d[4] += 1
    elif 2000 <= a < 2400:
        d[5] += 1
    elif 2400 <= a < 2800:
        d[6] += 1
    elif 2800 <= a < 3200:
        d[7] += 1
    else:
        d[8] += 1

cnt = 0
for i in range(8):
    if d[i]:
        cnt += 1

if cnt == 0:
    print(1, N)
else:
    print(cnt, cnt+d[8])
