N = int(input())
A = list(map(int, input().split()))

ans = 0
while True:
    A = [a//2 if a%2 == 0 else 0 for a in A]
    if not all(A):
        break
    ans += 1
print(ans)