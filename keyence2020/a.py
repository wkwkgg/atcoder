from math import ceil

H = int(input())
W = int(input())
N = int(input())

k = max(H, W)
print(ceil(N/k))
