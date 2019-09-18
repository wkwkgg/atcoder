S = input()

head, count = S[0], 0
ans = ""
for s in S:
    if head != s:
        ans += head + str(count)
        head, count = s, 1
    else:
        count += 1
else:
    ans += head + str(count)

print(ans)