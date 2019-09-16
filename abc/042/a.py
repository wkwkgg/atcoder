A, B, C = input().split()
print("YES" if "575" in {A+B+C, A+C+B, B+A+C, B+C+A, C+A+B, C+B+A} else "NO")