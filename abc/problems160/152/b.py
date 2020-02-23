A, B = map(int, input().split())

a = "{}".format(A) * B
b = "{}".format(B) * A

print(a if a < b else b)
