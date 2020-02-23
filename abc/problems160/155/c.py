from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

c = Counter(S)

max_cnt = 0
words = []
for s_i, cnt in sorted(c.items(), key=lambda x: x[1], reverse=True):
    if max_cnt <= cnt:
        max_cnt = cnt
        words.append(s_i)
    else:
        break

for word in sorted(words):
    print(word)
