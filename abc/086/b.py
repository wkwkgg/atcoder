from math import sqrt
N = int("".join(input().split()))
print('Yes' if N == int(sqrt(N))**2 else 'No')
