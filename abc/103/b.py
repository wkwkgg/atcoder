S = input()
T = input()

res = "No"
if S == T:
    res = "Yes"
else:
    N = len(S)
    for i in range(N):
        R = S[-i:] + S[:N-i]
        if T == R:
            res = "Yes"
            break
print(res)