from typing import List


# 繰り返し二乗法
#   - a^n % mod を高速に求める
#   - 計算量 O(log(n))
def modpow(a: int, n: int, mod: int) -> int:
    res = 1
    while n > 0:
        if n & 1 > 0:
            res = res * a % mod
        a = a**2 % mod
        n >>= 1
    return res


# 組み合わせ
#   - 組み合わせ nCk を求める
#   - 計算量 :  O(min(n-k, k))
def comb(n: int, k: int, mod: int) -> int:
    if n < 0 or k < 0 or n < k: return 0
    if n == 1 or k == 1: return 1

    x, y = 1, 1
    for i in range(1, min(n - k, k) + 1):
        x = x * (n - i + 1) % mod
        y = y * i % mod

    return x * modpow(y, mod - 2, mod) % mod


# 約数列挙
#   - 正整数 N の約数をリストで返す
#   - 計算量 : O(sqrt(N))
def divisors_list(n: int) -> List[int]:
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return divs


# 最大公約数 (GCD) を求める
#   - 計算量 : O(log(min(a,b)))
from fractions import gcd

# Python 3.5 で追加
#  - from math import gcd


# 最小公倍数 (LCM) を求める
def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)


# 3 つ以上の GCD, LCM を求める
from functools import reduce


# 3 つ以上の GCD を求める
def gcd_list(nums: List[int]) -> int:
    return reduce(gcd, nums)


# 3 つ以上の LCM を求める
def lcm_list(nums: List[int]) -> int:
    return reduce(lcm, nums, 1)