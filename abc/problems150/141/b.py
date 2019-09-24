S = list(input())
o = len(set(S[1::2]) - {'L', 'U', 'D'})
e = len(set(S[0::2]) - {'R', 'U', 'D'})
print("No" if o+e > 0 else "Yes")
