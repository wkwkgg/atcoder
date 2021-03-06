class UnionFind:
    def __init__(self, n: int):
        self.__n = n
        self.__par = list(range(self.__n))
        self.__size = [1 for _ in range(self.__n)]

    def root(self, x: int) -> int:
        if self.__par[x] == x:
            return x
        self.__par[x] = self.root(self.__par[x])
        return self.__par[x]

    def merge(self, x: int, y: int) -> bool:
        rx, ry = self.root(x), self.root(y)
        if rx == ry: return False

        if self.__size[rx] < self.__size[ry]:
            rx, ry = ry, rx

        self.__size[rx] += self.__size[ry]
        self.__par[ry] = rx
        return True

    def check(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def size(self, x: int) -> int:
        return self.__size[self.root(x)]


N, M = map(int, input().split())
ABm = [list(map(int, input().split())) for _ in range(M)]

ans = 0
for i in range(M):
    uf = UnionFind(N + 1)
    for j in range(M):
        if i == j: continue
        a, b = ABm[j]
        uf.merge(a, b)

    if uf.size(1) != N:
        ans += 1

print(ans)
