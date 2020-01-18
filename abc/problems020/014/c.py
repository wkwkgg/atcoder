# ABC014 : C - AtColor

N = int(input())
MAX = 10**6 + 2
memo = [0] * MAX

for _ in range(N):
    a, b = map(int, input().split())
    memo[a] += 1
    memo[b+1] -= 1

ans = 0
temp = 0
for i in range(MAX):
    temp += memo[i]
    ans = max(ans, temp)

print(ans)
