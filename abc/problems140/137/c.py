from collections import Counter

N = int(input())
S = ["".join(sorted(list(input()))) for _ in range(N)]

cnt = Counter(S)
print(sum(v*(v-1)//2 for v in cnt.values()))
