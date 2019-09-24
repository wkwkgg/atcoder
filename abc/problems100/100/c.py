N = int(input())
A = list(filter(lambda x: x % 2 == 0, map(int, input().split())))

ans = 0
for a in A:
    temp = 0
    while a % 2 == 0:
        a //= 2
        temp += 1
    ans += temp
print(ans)
