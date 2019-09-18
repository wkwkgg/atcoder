S = input()
K = int(input())

ans = 0
n = len(S)
if n >= K:
    subseq = set()
    for i in range(n-K+1):
        subseq.add(S[i:i+K])
    ans = len(subseq)
print(ans)