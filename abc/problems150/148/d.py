N = int(input())
a_list = list(map(int, input().split()))

res = 0
crr = 1
for a in a_list:
    if a == crr:
        crr += 1
    else:
        res += 1

print(-1 if res == N else res)
