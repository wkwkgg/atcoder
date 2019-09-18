A = int(input())
B = int(input())
C = int(input())

S = [A, B, C]
T = sorted(S, reverse=True)
for s in S:
    print(T.index(s) + 1)