import math
xs = [int(input()) for _ in range(5)]
print(sum(xs) + sum(sorted([math.ceil(x*0.1)*10 - x  for x in xs])[:4]))
