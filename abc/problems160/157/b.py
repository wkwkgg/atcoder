A = []
for _ in range(3):
    a = list(map(int, input().split()))
    A.append(a)

N = int(input())
Bn = set([int(input()) for _ in range(N)])

for b in Bn:
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                A[i][j] = 0

ans = False
if A[0][0] == A[1][1] == A[2][2] == 0:
    ans = True

if A[0][2] == A[1][1] == A[2][0] == 0:
    ans = True

# col
for i in range(3):
    cnt = 0
    for j in range(3):
        if A[j][i] == 0:
            cnt += 1
    if cnt == 3:
        ans = True

# row
for i in range(3):
    cnt = 0
    for j in range(3):
        if A[i][j] == 0:
            cnt += 1
    if cnt == 3:
        ans = True

print("Yes" if ans else "No")