N, M = map(int, input().split())
KS = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))

ans = 0
for i in range(2**N):
    status = [0] * N
    for j in range(N):
        if i >> j & 1:
            status[N - 1 - j] = 1

    possible = True
    for j in range(M):
        cnt_sw = sum(1 if status[k-1] == 1 else 0 for k in KS[j][1:])
        if cnt_sw%2 != P[j]:
            possible = False
    if possible:
        ans += 1
    
print(ans)