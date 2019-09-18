N = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

alice = sum(a[0::2])
bob = sum(a[1::2])
print(alice - bob)