N = int(input())

b, c = 1, 2+1
if N == 1:
    print(b)
if N == 2:
    print(c)
for _ in range(3, N+1):
    b, c = c, c+b
if N not in {1,2}: print(c)