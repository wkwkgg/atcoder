H = int(input())

ans = 1
if H > 1:
    prev, curr = 1, 2
    while 2**curr <= H:
        prev = curr
        curr = curr + 1

    ans = 2**prev + (2**prev-1)

print(ans)
