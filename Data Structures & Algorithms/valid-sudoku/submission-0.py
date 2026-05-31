class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        #check each column
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        # check 3x3 box
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        return True
