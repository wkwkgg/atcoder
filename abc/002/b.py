W = input()

ans = ""
for w in W:
    if w not in list("aiueo"):
        ans += w
print(ans)