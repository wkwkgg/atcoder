A, B = map(int, input().split())
S = input()
ans = "Yes"
if S[A] != '-' and S[A].count('-') != 1:
    ans = "No"
else:
    S = S.split('-')
    if len(S) != 2:
        ans = "No"
    if not(S[0].isdecimal() and S[1].isdecimal()):
        ans = "No"
print(ans)