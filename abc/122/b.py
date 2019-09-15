S = input()
res = 0
for i in range(len(S)):
    for j in range(i, len(S)):
        if all("ACGT".count(c) for c in S[i:j+1]):
            res = max(res, j - i + 1)
print(res)