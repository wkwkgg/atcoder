N = int(input())
A, B = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

print("YES" if len(P) + 2 == len(set(P + [A, B])) else "NO")
