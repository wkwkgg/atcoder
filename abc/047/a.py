a,b,c = map(int, input().split())
print("Yes" if max(a,b,c) == (sum([a,b,c]) - max(a,b,c)) else "No")