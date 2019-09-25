A, B, C = list(sorted(map(int, input().split())))

ans = 0
while (C-A) > 1:
    A += 2
    ans += 1

while (C-B) > 1:
    B += 2
    ans += 1

if A == C:
    if B != C:
        B += 2
        A += 1
        C += 1
        ans += 2
else:
    if B == C:
        A += 2
        B += 1
        C += 1
        ans += 2
    else:
        A += 1
        B += 1
        ans += 1
print(ans)
