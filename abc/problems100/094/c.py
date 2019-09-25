N = int(input())
X = list(map(int, input().split()))

x = sorted(X)
med1, med2 = x[N//2-1], x[N//2]

print("\n".join(str(med2) if X[i] < med2 else str(med1) for i in range(N)))
