N = int(input())

MOD = 10007
a1, a2, a3 = 0, 0, 1
ans = 0
if N < 3: ans = 0
elif N == 3: ans = a3
else:
    while N-3:
        a1,a2,a3 = a2,a3,(a1+a2+a3)%MOD
        N -= 1
    ans = a3
print(ans)
