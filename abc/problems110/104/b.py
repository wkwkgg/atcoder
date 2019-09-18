S = input()

res = "AC"
if S[0] != "A" or S.count("C") != 1:
    res = "WA"

if "C" not in S[2:-1]:
    res = "WA"

if res == "AC":
    for s in S[1:]:
        if s != "C" and s != s.lower():
            res = "WA"
            break
print(res)