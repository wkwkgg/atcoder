S = list(input())
T = list(input())

sd = dict()
td = dict()
ans = True
for s, t in zip(S, T):
    if s not in sd:
        sd[s] = t
    else:
        if sd[s] != t:
            ans = False
            break

    if t not in td:
        td[t] = s
    else:
        if td[t] != s:
            ans = False
            break

print("Yes" if ans else "No")
