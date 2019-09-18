N = int(input())
res = "Perfect"
if N <= 59:
    res = "Bad"
elif 60 <= N <= 89:
    res = "Good"
elif 90 <= N <= 99:
    res = "Great"
print(res)