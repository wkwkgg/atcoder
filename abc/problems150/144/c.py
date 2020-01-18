N = int(input())

divs = set()
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        q = N // i
        divs.add((min(q, i), max(q, i)))

res = float("inf")
for a, b in divs:
    res = min(res, a+b-2)

print(res)
