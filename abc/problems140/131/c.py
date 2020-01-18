from fractions import gcd

A, B, C, D = map(int, input().split())

cnt_c = B//C - (A-1)//C
cnt_d = B//D - (A-1)//D

lcm = C * D // gcd(C, D)
cnt_cd = B//lcm - (A-1)//lcm

divisible = cnt_c + cnt_d - cnt_cd
print(B-A+1-divisible)
