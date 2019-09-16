N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for _ in range(M)]

for p,x in PX:
    print(sum(T) - T[p-1] + x)