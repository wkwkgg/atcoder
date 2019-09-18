def ss(s):
    return s[:len(s)//2] == s[len(s)//2:]

S = input()
N = len(S)
for i in range(1, N-1):
    if ss(S[:N-i]):
        ans = N-i
        break
print(ans)