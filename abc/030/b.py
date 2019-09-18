N, M = map(int, input().split())

n = N-12 if N > 12 else N
deg_n = (n*60+M)*360 / (12*60)
deg_m = M*360 / 60
diff = abs(deg_n - deg_m)
if diff > 180:
    print(360 - diff)
else:
    print(diff)