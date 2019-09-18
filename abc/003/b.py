S = input()
T = input()
K = list("atcoder")

ans = True
for s,t in zip(S,T):
    if s == t:
        continue
    else:
        if s == "@":
            if t not in K:
                ans = False
                break
        elif t == "@":
            if s not in K:
                ans = False
                break
        else:
            ans = False
            break

print("You can win" if ans else "You will lose")

