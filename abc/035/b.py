S = input()
T = int(input())

d = abs(S.count("L") - S.count("R")) + abs(S.count("U") - S.count("D"))

if T == 2:
    print(max(d - S.count("?"), (d - S.count("?"))%2))
else:
    print(d + S.count("?"))