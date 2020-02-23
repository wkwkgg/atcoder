from math import ceil

D, G = map(int, input().split())
Pd, Cd = [0] * D, [0] * D

for i in range(D):
    Pd[i], Cd[i] = map(int, input().split())


ans = float("inf")
# 外側のループ Pd[i] を使うかどうかについてのループ
# e.g. D==2 の場合
#   0 -> 00 : 両方使わない
#   1 -> 01 : 0 番目を使う
#   2 -> 10 : 1 番目を使う
#   3 -> 11 : 両方使う
for i in range(1 << D):
    score, solved, unsolved = 0, 0, 0
    # 各 bit に対してシフトしていく
    # 1 を j シフトさせる (D-1) 回シフトさせる
    # i を右端から 1 ビットずつ見ていく
    for j in range(D):
        if i & (1 << j):
            # j 番目の問題を解く
            # 一部だけ解くことはないので、全部得点を得る
            score += 100 * (j+1) * Pd[j] + Cd[j]
            # 解いた問題数をカウント
            solved += Pd[j]
        else:
            # j 番目の問題を解かない場合, 解かない問題で最もスコアの高いものを保存
            # 解かない場合、部分的に使うので 100*(j+1) のスコアが高いものから利用する
            unsolved = j

    # 目標に到達してない場合に部分的に問題を解く (ボーナス無しで unsolved 番目の問題を一部解く)
    rest = G - score
    if rest > 0:
        # unsolved 番目の問題を部分的に利用して解く
        # k は unsolved 番目の問題を 1 問解いたときの得点
        k = 100 * (unsolved+1)
        # unsolved 番目の問題を全て解いても rest が 0 にならない場合、組み合わせが不適
        if k * Pd[unsolved] < rest:
            continue
        solved += ceil(rest/k)

    ans = min(ans, solved)

print(ans)
