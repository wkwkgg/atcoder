Sa = list(input())
Sb = list(input())
Sc = list(input())

now = Sa.pop(0)
ans = ""

while True:
    if now == "a":
        if not Sa:
            ans = "A"
            break
        now = Sa.pop(0)
    elif now == "b":
        if not Sb:
            ans = "B"
            break
        now = Sb.pop(0)
    else:
        if not Sc:
            ans = "C"
            break
        now = Sc.pop(0)
print(ans)