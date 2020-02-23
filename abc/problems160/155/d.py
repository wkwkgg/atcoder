from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


# 入力
N, K = map(int, input().split())
An = list(map(int, input().split()))

P, Z, N = [], [], []
for i in range(N):
    if An[i] == 0:
        Z.append(An[i])
    elif An[i] > 0:
        P.append(An[i])
    else:
        N.append(An[i])

# An[i] に含まれる数について正, 0, 負をカウント
plen, zlen, nlen = len(P), len(Z), len(N)

# 積が 正, 0, 負 の数をカウント
neg_len = plen * nlen
zero_len = plen * zlen + nlen * zlen
pos_len = cmb(plen, 2) + cmb(nlen, 2)
