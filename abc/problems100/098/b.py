N = int(input())
S = input()

ans = 0
for i in range(1, N-1):
    ans = max(ans, len(set(list(S[:i])) & set(list(S[i:]))))
print(ans)