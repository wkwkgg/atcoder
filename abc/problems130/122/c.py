N, Q = map(int, input().split())
S = input()
LR = [list(map(int, input().split())) for _ in range(Q)]

cnt, acc = [0] * N, 0
for i in range(1, N):
    if S[i-1:i+1] == "AC":
        acc += 1
    cnt[i] = acc

for l, r in LR:
    print(cnt[r-1] - cnt[l-1])
