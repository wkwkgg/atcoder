N = int(input())
S = list(input())

head = S[0]
res = 1
for i in range(1, N):
    if S[i] != head:
        res += 1
        head = S[i]

print(res)
