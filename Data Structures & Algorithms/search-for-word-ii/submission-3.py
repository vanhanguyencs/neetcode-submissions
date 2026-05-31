class Solution:
    """
    option 1:
    for each word:
        perform dfs
    tc: O(M*N*L)

    option 2:
    use trie to store list of word
    for each cel in grid:
        perform dfs
    tc: O(M*N)
    """
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.buildTrie(words)
        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, root, res, m , n)
        return res
            
    def dfs(self, board, i, j, root, res, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == '.':
            return
        if root.word is not None:
            res.append(root.word)
            root.word = None
        #mark visited
        tmp = board[i][j]
        node = root.children[ord(tmp) - ord('a')]
        if node is None:
            return
        if node.word is not None:
            res.append(node.word)
            node.word = None
        board[i][j] = '.'
        self.dfs(board, i + 1, j, node, res, m, n)
        self.dfs(board, i - 1, j, node, res, m, n)
        self.dfs(board, i, j + 1, node, res, m, n)
        self.dfs(board, i, j - 1, node, res, m, n)
        board[i][j] = tmp
        

        
    
    def buildTrie(self, words: List[str]) -> TrieNode:
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                i = ord(c) - ord('a')
                if cur.children[i] is None:
                    cur.children[i] = TrieNode()
                cur = cur.children[i]
            cur.word = word
        return root
    


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None
