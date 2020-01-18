def conv(c, n):
    p = ord(c) + n
    if p > ord("Z"):
        p -= (ord("Z") - ord("A") + 1)
    return chr(p)


N = int(input())
S = list(input())

print("".join(conv(c, N) for c in S))
