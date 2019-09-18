M = int(input()) / 1000

ans = 0
if M < 0.1:
    ans = 0
elif 0.1 <= M <= 5:
    ans = int(M * 10)
elif 6 <= M <= 30:
    ans = int(M) + 50
elif 35 <= M <= 70:
    ans = (int(M) - 30)//5+80
elif 70 < M:
    ans = 89
print("{:02}".format(ans))