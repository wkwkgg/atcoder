N = int(input())
S = input()

s = "b"
n = 1
ans = 0 if len(S) == 1 and S == "b" else -1
while len(s) < N:
    if n%3 == 1: s = "a" + s + "c"
    elif n%3 == 2: s = "c" + s + "a"
    else: s = "b" + s + "b"
    if s == S:
        ans = n
        break
    n += 1

print(ans)