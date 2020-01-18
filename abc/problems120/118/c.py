# ABC118 : C - Monsters Battle Royale

from fractions import gcd
from functools import reduce


def gcd_list(nums):
    return reduce(gcd, nums)


N = int(input())
A = sorted(list(map(int, input().split())))

print(gcd_list(A))
