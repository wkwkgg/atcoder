N = input()
left = len(set(list(N[1:]))) == 1
right = len(set(list(N[:3]))) == 1
print("Yes" if left or right else "No")
