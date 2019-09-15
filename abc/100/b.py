D, N = map(int, input().split())
d = 100**D
seq = [i for i in range(1, 100)] + [101]

if D:
    seq = [x*(100**D) for x in seq]

print(seq[N-1])
