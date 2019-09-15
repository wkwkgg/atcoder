A, B, C = map(int, input().split())
K = int(input())

M = max(A, B, C)
P = 2**K * M
print(P + sum([A,B,C]) - M)
