S = list(input())
N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

for l,r in P:
    S[l-1:r] = S[l-1:r][::-1]
print("".join(S))