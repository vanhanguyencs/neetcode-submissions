class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        ["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]
        """
        def dfs(i, j, visited, idx):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx] or visited[i][j]:
                return False
            if idx == len(word) - 1 and board[i][j] == word[idx]:
                return True
            visited[i][j] = True
            found = (
                dfs(i + 1, j, visited, idx + 1)
                or dfs(i - 1, j, visited, idx + 1)
                or dfs(i, j + 1, visited, idx + 1)
                or dfs(i, j - 1, visited, idx + 1)
            )
            visited[i][j] = False
            return found
            
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = [[False] * n for _ in range(m)]
                    if dfs(i, j, visited, 0):
                        return True
        return False
