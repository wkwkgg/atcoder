S = input()[::-1]
ws = ["dream", "dreamer", "erase", "eraser"]
ws = [w[::-1] for w in ws]

s = S
ans = True
T = ""
while S != T:
    if s[:7] == ws[1]:
        T, s = T + ws[1], s[7:]
    elif s[:6] == ws[3]:
        T, s = T + ws[3], s[6:]
    elif s[:5] == ws[2]:
        T, s = T + ws[2], s[5:]
    elif s[:5] == ws[0]:
        T, s = T + ws[0], s[5:]
    else:
        ans = False
        break

print("YES" if ans else "NO")
