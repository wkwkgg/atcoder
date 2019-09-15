A, B, K = map(int, input().split())
a = [i for i in range(A, min(A+K,B))]
b = [i for i in range(max(A,B-K+1), B+1)]

for x in sorted(list(set(a + b))):
    print(x)