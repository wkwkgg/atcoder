# ABC123 : C - Five Transportations
from math import ceil

ins = [int(input()) for _ in range(6)]
N, *xs = ins
k = min(xs)
print(4 + ceil(N/k))
