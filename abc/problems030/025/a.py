from itertools import product
S = list(input())
N = int(input())

print([a+b for a,b in product(S, S)][N-1])