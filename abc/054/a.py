A, B = map(int, input().split())

A = 14 if A == 1 else A
B = 14 if B == 1 else B

ans = "Draw"
if A > B:
    ans = "Alice"
if A < B:
    ans = "Bob"

print(ans)