A, B, C, K = map(int, input().split())
S, T = map(int, input().split())
s = S*A + T*B
if S+T >= K:
    s -= C*(S+T)
print(s)