A, B = map(int, input().split())
ans = 0
for x in range(A, B+1):
    if int("".join(list(reversed(str(x))))) == x:
        ans += 1
print(ans)