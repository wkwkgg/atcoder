A, B, C, D = map(int, input().split())

start = C if A < C else A
end = B if B < D else D
ans = 0 if start > end else end - start
print(ans)
