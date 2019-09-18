S = input()
ans = ""
for s in S:
    if s in {'0', '1'}:
        ans += s
    else:
        ans = ans[:-1]
print(ans)