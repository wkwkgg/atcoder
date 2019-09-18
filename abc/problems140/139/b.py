A, B = map(int, input().split())

res = 0
outlet = 1
while outlet < B:
    outlet -= 1
    outlet += A
    res += 1
print(res)