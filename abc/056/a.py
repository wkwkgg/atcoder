a, b = input().split()

if a == "H":
    ans = "H" if b == "H" else "D"
else:
    ans = "H" if b == "D" else "D"

print(ans)