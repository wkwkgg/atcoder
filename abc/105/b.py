N = int(input())

ans = "No"
if N < 4:
    ans = "No"
elif N%4 == 0 or N%7 == 0:
    ans = "Yes"
else:
    for a in range(0, 25):
        for b in range(0, 15):
            if 4*a + 7*b == N:
                ans = "Yes"
                break
print(ans)
