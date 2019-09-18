N, A, B = map(int, input().split())
SD = [input().split() for _ in range(N)]

current = 0
for s, d in SD:
    k = int(d)
    if s == "East":
        if A <= k <= B:
            current += k
        elif k < A:
            current += A
        else:
            current += B
    else:
        if A <= k <= B:
            current -= k
        elif k < A:
            current -= A
        else:
            current -= B

direction = "East" if current > 0 else "West"

if current == 0:
    print(0)
else:
    print(direction, abs(current))