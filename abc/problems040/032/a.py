A = int(input())
B = int(input())
N = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd (a, b)


r = lcm(A, B)
i = 1
ans = r*i
while ans < N:
    ans, i = r*i, i+1
print(ans)