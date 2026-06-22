class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        DFS or BFS from O from 4 edges,
        update it to different character to mark that they are not surrounded.
        then iterate all cell to update O to X, and A to O
        """
        def dfs(r, c):
            if r < 0 or c< 0 or r >= m or c >= n or board[r][c] != 'O':
                return
            board[r][c] = 'A'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        m, n = len(board), len(board[0])

        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
             
        
        