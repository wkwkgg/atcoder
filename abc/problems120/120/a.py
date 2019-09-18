a,b,c = map(int, input().split())

if a > b:
    res = 0
else:
    if a*c <= b:
        res = c
    else:
        res = b // a

print(res)
