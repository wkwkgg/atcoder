from itertools import permutations

N = int(input())
Pn = tuple(map(int, input().split()))
Qn = tuple(map(int, input().split()))

p, q = 0, 0
for i, t in enumerate(permutations(range(1, N+1), N)):
    if t == Pn:
        p = i
    if t == Qn:
        q = i

print(abs(p - q))
