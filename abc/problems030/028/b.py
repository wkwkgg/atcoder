S = input()
res = {x: 0 for x in list("ABCDEF")}

for s in S:
    res[s] += 1

print(" ".join(str(res[k]) for k in sorted(res.keys())))
