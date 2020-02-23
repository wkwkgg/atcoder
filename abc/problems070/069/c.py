# C - 4-adjacent

N = int(input())
An = list(map(int, input().split()))

m2, m4, rest = [], [], []
for i in range(N):
    if An[i] % 2 == 0 and An[i] % 4 != 0:
        m2.append(An[i])
    elif An[i] % 4 == 0:
        m4.append(An[i])
    else:
        rest.append(An[i])

ans = "No"
if len(m4) == len(rest):
    ans = "Yes"
if len(m4) == len(rest)-1 and len(m2) == 0:
    ans = "Yes"
if not len(rest):
    ans = "Yes"

print(ans)
