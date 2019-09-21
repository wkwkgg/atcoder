S = input()
s = list(map(int, list(S)))

ans = 0
op_cnt = len(s) - 1
for i in range(2 ** op_cnt):
    op = ["-"] * op_cnt
    for j in range(op_cnt):
        if (i >> j) & 1:
            op[op_cnt - 1 - j] = "+"
    op += ["-"]

    expr = "".join([n+o for n, o in zip(S, op)]).replace("-", "")
    ans += eval(expr)
print(ans)
