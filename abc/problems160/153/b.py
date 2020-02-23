H, N = map(int, input().split())
An = list(map(int, input().split()))

print("Yes" if sum(An) >= H else "No")
