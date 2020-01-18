W, H, X, Y = map(int, input().split())

print(W * H / 2, 1 if W == 2*X and H == 2*Y else 0)
