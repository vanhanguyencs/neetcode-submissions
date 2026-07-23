class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not node.children[i]:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not node.children[i]:
                return False
            node = node.children[i]
        return node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not node.children[i]:
                return False
            node = node.children[i]
        return True

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False
        
        