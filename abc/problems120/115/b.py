N = int(input())
P = sorted([int(input()) for _ in range(N)])
print(sum(P[:N-1]) + P[-1]//2)

