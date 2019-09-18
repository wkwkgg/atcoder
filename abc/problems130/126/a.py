N, K = map(int, input().split())
S = input()
print("".join([s if i != K else s.lower() for i,s in enumerate(list(S), 1)]))