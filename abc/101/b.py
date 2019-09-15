N = input()
sn = sum(map(int, list(N)))
print("Yes" if int(N)%sn == 0 else "No")