class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        DFS
        BFS
        """
        def addCell(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or (r, c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            q.append([r, c])
        
        q = deque()
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
        


        
