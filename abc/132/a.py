S = input()

res = "Yes"
s = set(list(S))
if len(s) != 2:
    res = "No"
else:
    a, b = s
    if not S.count(a) == S.count(b) == 2:
        res = "No"
print(res)