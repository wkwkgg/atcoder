N = int(input())
An = list(map(int, input().split()))

ans = "APPROVED"
for i in range(N):
    if An[i] % 2 != 0:
        continue

    if An[i] % 3 == 0 or An[i] % 5 == 0:
        continue

    ans = "DENIED"

print(ans)
