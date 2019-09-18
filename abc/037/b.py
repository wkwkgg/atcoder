N, Q = map(int, input().split())
LRT = [list(map(int, input().split())) for _ in range(Q)]

seq = [0 for _ in range(N)]
for l,r,t in LRT:
    seq[l-1:r] = [t] * (r - l + 1)

print("\n".join(map(str, seq)))
