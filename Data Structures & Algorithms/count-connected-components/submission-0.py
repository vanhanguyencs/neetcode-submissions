class DSU:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.ranking = [0] * size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        a0 = self.find(x)
        a1 = self.find(y)

        if a0 == a1:
            return False

        if self.ranking[a0] == self.ranking[a1]:
            self.ranking[a0] += 1
            self.parent[a1] = a0  # merge a1 into a0
        elif self.ranking[a0] > self.ranking[a1]:
            self.parent[a1] = a0
        else:
            self.parent[a0] = a1

        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = n
        dsu = DSU(n)
        for u, v in edges:
            if dsu.union(u, v):
                ans -= 1
        return ans
        