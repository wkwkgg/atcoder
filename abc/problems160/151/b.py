N, K, M = map(int, input().split())
An = list(map(int, input().split()))

rest = M*N - sum(An)
if rest <= K:
    print(max(0, rest))
else:
    print(-1)
