s = int(input())

l, i = [s], 1
ans = 0
while True:
    n = s//2 if s%2 == 0 else 3*s+1
    i += 1
    if n in l:
        ans = i
        break
    s = n
    l.append(n)
print(ans)