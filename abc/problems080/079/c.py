ABCD = input()
S = list(ABCD)
op_cnt = len(S) - 1

ans = None
for i in range(2**op_cnt):
    op = ["+"] * op_cnt
    for j in range(op_cnt):
        if i >> j & 1:
            op[op_cnt - j - 1] = "-"
    expr = S[0] + "".join(o+s for s,o in zip(S[1:], op))
    if eval(expr) == 7:
        ans = expr + "=7"
        break
print(ans)