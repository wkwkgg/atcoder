# ABC011 : C - 123引き算

N = int(input())
NG = [int(input()) for _ in range(3)]

ans = True
if N in NG:
    ans = False
else:
    for i in range(100):
        temp = N
        xs = [N-3, N-2, N-1]

        for x in xs:
            if x in NG:
                continue
            N = x
            break

        if temp == N:
            ans = False
            break

    if N > 0:
        ans = False

print("YES" if ans else "NO")
