class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        BFS
        1 0 1
        0 2 0
        1 0 1
        """
        def addCell(i, j):
            nonlocal total_rotten
            if min(i, j) < 0 or i >= m or j >= n or grid[i][j] == 0 or grid[i][j] == 2:
                return
            grid[i][j] = 2
            total_rotten += 1
            q.append((i, j))
        q = deque()
        m, n = len(grid), len(grid[0])
        total_rotten = 0

        total_fruit = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    total_fruit += 1
        
        nbr_minute = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            nbr_minute += 1
        
        return max(0, nbr_minute - 1) if total_rotten == total_fruit else -1