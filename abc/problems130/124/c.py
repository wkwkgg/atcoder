S = input()

size = len(S)
n = "".join("1" if i % 2 == 0 else "0" for i in range(size))

nc, mc = 0, 0
for i in range(size):
    if S[i] == n[i]:
        nc += 1
    else:
        mc += 1

print(min(nc, mc))
