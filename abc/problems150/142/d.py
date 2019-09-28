from fractions import gcd

A, B = map(int, input().split())


def divisor(n):
    i = 1
    xs = []
    while i * i <= n:
        if n % i == 0:
            xs.append(i)
            xs.append(n//i)
        i += 1
    return set(xs)


ad, bd = divisor(A), divisor(B)
xs = list(sorted(ad & bd))

ans = [1]
for x in xs:
    flag = True
    for k in ans:
        if gcd(x, k) != 1:
            flag = False
            break
    if flag:
        ans.append(x)
print(len(set(ans)))
