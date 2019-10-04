from collections import defaultdict

MOD = 10**9 + 7
facts = defaultdict(int)


def factorize(n):
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
                facts[i] += 1
    if temp != 1:
        facts[temp] += 1


N = int(input())
for x in range(1, N+1):
    factorize(x)

ans = 1
for v in facts.values():
    ans *= (v+1)
    ans %= MOD

print(ans)
