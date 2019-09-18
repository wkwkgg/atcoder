from math import pi

N = int(input())
R = sorted([int(input()) for _ in range(N)])[::-1]
print((sum(r**2 for r in R[::2]) - sum(r**2 for r in R[1::2])) * pi)
