A, B = map(int, input().split())
K = abs(A+B) // 2

if abs(A-K) == abs(B-K):
    print(K)
else:
    print("IMPOSSIBLE")