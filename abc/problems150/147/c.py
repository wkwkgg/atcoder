from itertools import product
N = int(input())

An = []
Xn, Yn = [], []

for i in range(N):
    An.append(int(input()))
    Xn.append([])
    Yn.append([])
    for j in range(An[i]):
        x, y = map(int, input().split())
        Xn[i].append(x)
        Yn[i].append(y)

ans = 0
for prod in product("01", repeat=N):
    # bits : i 番目の bit が 1 なら i は正直者として, 仮定する
    bits = list(map(int, prod))
    flag = True

    # bits のリストで矛盾が無いかを調べる
    for i in range(N):
        # i が不親切と仮定するなら,調べる必要はない
        if bits[i] != 1:
            continue

        # B[i] == 1, つまり i が正直者である場合, A_i 個の証言を調べる
        for j in range(An[i]):
            # 「i の証言 : y_ij = 1 のとき x_ij == 1 (正直者である)」に矛盾がある場合
            if Yn[i][j] == 1 and bits[Xn[i][j]-1] == 0:
                flag = False

            # 「i の証言 : y_ij = 0 のとき x_ij == 0 (不親切である)」に矛盾がある場合
            elif Yn[i][j] == 0 and bits[Xn[i][j]-1] == 1:
                flag = False

    # flag が True => bits のリストで矛盾がない
    if flag:
        ans = max(ans, bits.count(1))

print(ans)
