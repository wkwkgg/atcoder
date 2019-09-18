S = input()
ans = float("inf")
for s1, s2, s3 in zip(S[:-2], S[1:-1], S[2:]):
    ans = min(ans, abs(753 - int(s1 + s2 + s3)))
print(ans)