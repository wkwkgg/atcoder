X = input()

ans = len(X)
X = X[::-1]
i = 0
while ans:
    if X[i] in list("oku"):
        ans -= 1
    elif ans >= 2 and X[i:i+2] == "hc":
        ans -= 2
    else:
        break
    i += 1

print("YES" if not ans else "NO")