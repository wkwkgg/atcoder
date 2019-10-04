# ABC109 : C - Skip
from fractions import gcd
from functools import reduce

N, X = map(int, input().split())
XS = list(map(int, input().split()))


def gcd_list(nums):
    return reduce(gcd, nums)


ns = [abs(x-X) for x in XS]
print(gcd_list(ns))
