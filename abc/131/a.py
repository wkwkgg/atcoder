S = input()
print("Good" if all(a != b for a,b in zip(S[:3], S[1:])) else "Bad")
