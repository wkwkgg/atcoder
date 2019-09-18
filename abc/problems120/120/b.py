a,b,k = map(int, input().split())

res = 1
for i in range(1, min(a,b)+1)[::-1]:
    if a%i == 0 and b%i == 0:
        k -= 1
        if k == 0:
            res = i
            break

print(res)