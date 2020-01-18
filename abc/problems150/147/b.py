S = input()


def count(s1, s2):
    res = 0
    for t1, t2 in zip(s1, s2):
        if t1 != t2:
            res += 1

    return res


res = 0
lenS = len(S)
if lenS > 1:
    if lenS % 2 == 0:
        s1, s2 = S[lenS//2:], S[:lenS//2][::-1]
        res = count(s1, s2)
    else:
        s1, s2 = S[lenS//2:], S[:lenS//2+1][::-1]
        res = count(s1, s2)

print(res)
