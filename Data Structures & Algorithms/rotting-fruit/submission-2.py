class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        BFS
        1 0 1
        0 2 0
        1 0 1
        """
        def addCell(i, j):
            nonlocal fresh
            if min(i, j) < 0 or i >= m or j >= n or grid[i][j] == 0 or grid[i][j] == 2:
                return
            grid[i][j] = 2
            fresh -= 1
            q.append((i, j))
        q = deque()
        m, n = len(grid), len(grid[0])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        nbr_minute = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            nbr_minute += 1
        
        return nbr_minute - 1 if fresh == 0 else -1