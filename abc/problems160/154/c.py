N = int(input())
An = list(map(int, input().split()))

if len(set(An)) == len(An):
    ans = "YES"
else:
    ans = "NO"

print(ans)
