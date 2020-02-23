# C - Multiple Clocks

from functools import reduce
from fractions import gcd


def lcm_base(x, y):
    return (x * y) // gcd(x, y)


def lcm(numbers):
    return reduce(lcm_base, numbers, 1)


N = int(input())
Tn = [int(input()) for _ in range(N)]

print(lcm(Tn))
