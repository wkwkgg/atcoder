# C - Linear Approximation
def f(l, b):
    return sum(abs(x-b) for x in l)


N = int(input())
X = list(map(int, input().split()))

xs = [x-i for i, x in enumerate(X, 1)]
if N % 2 != 0:
    b = sorted(xs)[N//2]
    print(f(xs, b))
else:
    b1 = sorted(xs)[N//2-1]
    b2 = sorted(xs)[N//2]
    print(min(f(xs, b1), f(xs, b2)))
