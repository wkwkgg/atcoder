N = int(input())
A = [int(input()) for _ in range(N)]

if N == 2:
    print("\n".join(map(str, A[::-1])))
else:
    a = sorted(A)
    maxv1 = a[-1]
    maxi1 = A.index(maxv1)
    maxv2 = a[-2]

    print("\n".join(map(str, [maxv1 if i != maxi1 else maxv2 for i in range(N)])))
