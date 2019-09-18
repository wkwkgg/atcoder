N = int(input())
n = list(filter(lambda x: x >= N, [111*i for i in range(1, 10)]))
print(n[0])
