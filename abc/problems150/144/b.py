from itertools import product
N = int(input())
print("Yes" if N in {a*b for a,
                     b in product(range(1, 10), range(1, 10))} else "No")
