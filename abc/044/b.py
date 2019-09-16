w = input()
s = set(list(w))

ans = "Yes"
for i in s:
    if w.count(i)%2 != 0:
        ans = "No"
        break
print(ans)
