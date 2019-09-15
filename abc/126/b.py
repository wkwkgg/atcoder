S = input()

head, tail = S[:2], S[2:]
if 1 <= int(head) <= 12:
    print("AMBIGUOUS" if 1 <= int(tail) <= 12 else "MMYY")
else:
    print("YYMM" if 1 <= int(tail) <= 12 else "NA")