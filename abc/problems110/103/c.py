from fractions import gcd
from functools import reduce


def lcm(x, y):
    return (x * y) // gcd(x, y)


def lcm_list(nums):
    return reduce(lcm, nums, 1)


N = int(input())
A = list(map(int, input().split()))

x = lcm_list(A) - 1
print(sum(x % a for a in A))
