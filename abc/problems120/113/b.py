N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

ans, ans_abs = -1, float("inf")
H = [(i+1, T - h*0.006) for i, h in enumerate(H)]
for i, h in H:
    if ans_abs > abs(A - h):
        ans = i
        ans_abs = abs(A - h)
print(ans)
