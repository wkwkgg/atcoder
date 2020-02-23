from math import ceil

N, A, B = map(int, input().split())
Hn = [int(input()) for _ in range(N)]

# K 回ですべての敵を倒せるか? という決定問題に落とし込む
# K は二分探索で求めることで時間内に解くことができる O(logN)

# K 回の爆発で x 回中心に選択されるとすると、
# 任意の敵のダメージは Ax + B(K-x) = (A-B)x + BK
# BK は固定ダメージ, 中心として選ばれる回数は ceil((h_i-BK)/(A-B))
# 単調性を用いて K を0 から十分に大きい数(10**12) の間で二分探索させる


def f(k):
    temp = 0
    for i in range(N):
        rest = Hn[i] - B*k
        if rest > 0:
            temp += ceil((Hn[i] - B*k) / (A-B))
    return (temp <= k)


def binsearch(ok, ng):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(binsearch(10**12, 0))
