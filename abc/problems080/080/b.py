N = input()
f = sum(map(int, list(N)))
print('Yes' if int(N)%f == 0 else 'No')