N = int(input())
print(sorted(list(set([int(input()) for _ in range(N)])), reverse=True)[1])