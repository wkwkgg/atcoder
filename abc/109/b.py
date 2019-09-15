N = int(input())
W = [input() for _ in range(N)]

ans = "Yes"
if len(set(W)) != N:
    ans = "No"
else:
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            ans = "No"
            break
print(ans)