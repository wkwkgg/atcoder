N = int(input())
H = list(map(int, input().split()))[::-1]

ans = True
for i in range(N-1):
    if H[i] < H[i+1]:
        if H[i+1] - H[i] > 1:
            ans = False
        else:
            H[i+1] -= 1
print("Yes" if ans else "No")
