class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for k in range(26):
                        if cur.children[k] is None:
                            continue
                        if dfs(i+1, cur.children[k]):
                            return True
                    return False
                else:
                    idx = ord(c) - ord('a')
                    if cur.children[idx] is not None:
                        cur = cur.children[idx]
                    else:
                        return False
                    
            return cur.endOfWord
        
        return dfs(0, self.root)
            


            


        
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False