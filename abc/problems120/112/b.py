N, T = map(int, input().split())
ct = list(filter(lambda x: x[1] <= T, [list(map(int, input().split())) for _ in range(N)]))
ct = sorted(ct, key=lambda x: x[0])
if not ct:
    print('TLE')
else:
    print(ct[0][0])