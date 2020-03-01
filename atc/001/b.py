class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]

    def root(self, x: int) -> int:
        if self.par[x] == x:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self, x: int, y: int):
        root_x, root_y = self.root(x), self.root(y)
        if root_x != root_y:
            self.par[root_x] = root_y

    def is_same(self, x: int, y: int) -> bool:
        root_x, root_y = self.root(x), self.root(y)
        return root_x == root_y


N, Q = map(int, input().split())
u = UnionFind(N)
PABq = [list(map(int, input().split())) for _ in range(Q)]

for query, a, b in PABq:
    if query == 0:
        u.unite(a, b)
    else:
        res = u.is_same(a, b)
        print("Yes" if res else "No")