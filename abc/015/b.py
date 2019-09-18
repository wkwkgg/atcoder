from math import ceil
N = int(input())
A = list(map(int, input().split()))

print(ceil(sum(A) / (len(A) - A.count(0))))