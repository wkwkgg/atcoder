N = int(input())
S = list(input())

res = False
if N % 2 == 0:
    T = S[:(N//2)]
    if T+T == S:
        res = True

print("Yes" if res else "No")
