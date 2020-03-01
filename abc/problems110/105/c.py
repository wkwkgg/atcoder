N = int(input())

res = []
if N != 0:
    while N != 0:
        q, r = divmod(N, -2)

        if r in {0, 1}:
            N = q
        else:
            r = N - (-2) * (q + 1)
            N = q + 1
        res.append(r)
else:
    res.append(0)

print("".join(list(map(str, res[::-1]))))