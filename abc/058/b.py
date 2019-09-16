O = input()
E = input()

ol, el = len(O), len(E)

ans = ""
for i in range(min(ol, el)):
    ans += O[i] + E[i]

if ol != el:
    if ol > el:
        ans += O[-1]
    else:
        ans += E[-1]
print(ans)