N = int(input())

m,s = divmod(N, 60)
h,m = divmod(m, 60)
print("{:02}:{:02}:{:02}".format(h,m,s))