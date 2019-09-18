H, W = map(int, input().split())
a = ["#" + input() + "#" for _ in range(H)]

print("#"*(W+2))
for x in a:
    print(x)
print("#"*(W+2))