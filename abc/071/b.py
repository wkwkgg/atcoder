S = set(list(input()))
a = {chr(ord('a') + i) for i in range(26)}
d = a - S
print('None' if not len(d) else min(d))
