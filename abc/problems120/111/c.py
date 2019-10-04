# ABC111 : C - /\/\/\/
from collections import Counter


def f(d, val):
    res = 0
    for elem, amount in d.items():
        if elem == val:
            continue
        res += amount
    return res


N = int(input())
V = list(map(int, input().split()))

e = Counter(V[0::2])
o = Counter(V[1::2])

e1 = e.most_common()[0]
o1 = o.most_common()[0]

ans = 0
if e1 != o1:
    ans += f(e, e1[0])
    ans += f(o, o1[0])
else:
    if e1[1] > o1[1]:
        if len(o) < 2:
            ans += o1[1]
        else:
            ans += f(o, o.most_common()[1][0])
        ans += f(e, e1[0])
    elif e1[1] < o1[1]:
        if len(e) < 2:
            ans += e1[1]
        else:
            ans += f(e, e.most_common()[1][0])
        ans += f(o, o1[0])
    else:
        if len(o) == len(e) == 1:
            ans += e1[1]
        elif len(o) == 1:
            ans += f(e, e.most_common()[1][0])
        elif len(e) == 1:
            ans += f(o, o.most_common()[1][0])
        else:
            e2 = e.most_common()[1]
            o2 = o.most_common()[1]

            if e2[1] > o2[1]:
                ans += f(e, e2[0])
                ans += f(o, o1[0])
            else:
                ans += f(e, e1[0])
                ans += f(o, o2[0])
print(ans)
