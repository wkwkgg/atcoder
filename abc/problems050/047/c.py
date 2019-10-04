S = input()

s = S[0]
j = 0
for i in range(1, len(S)):
    if s[j] == S[i]:
        continue
    s += S[i]
    j += 1

print(len(s) - 1)
