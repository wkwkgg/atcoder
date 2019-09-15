N, M, X, Y = map(int, input().split())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

x, y = max(xs), min(ys)
print("No War" if y - x >= 1 and X < y < Y else "War")

