N, M = map(int, input().split())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


divs = sorted(make_divisors(M), reverse=True)

ans = 1
for div in divs:
    res = div if div*N <= M else 1
    ans = max(ans, res)

print(ans)
