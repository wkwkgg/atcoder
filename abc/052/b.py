N = int(input())
S = input()
res = [0] + [0] * len(S)

for i,s in enumerate(S, 1):
    if s == "I":
        res[i] = res[i-1] + 1
    else:
        res[i] = res[i-1] - 1

print(max(res) if max(res) > 0 else 0)