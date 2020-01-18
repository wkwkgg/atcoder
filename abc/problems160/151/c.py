N, M = map(int, input().split())
ac, wa = 0, 0

ac_list = [0] * 10**6
wa_list = [0] * 10**6
for i in range(M):
    p, s = input().split()

    if ac_list[int(p)]:
        continue

    if s == "AC":
        ac_list[int(p)] = 1
        ac += 1
        wa += wa_list[int(p)]
    else:
        wa_list[int(p)] += 1

print(ac, wa)
