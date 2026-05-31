class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch_map = defaultdict(int)
        m, n = len(s), len(t)
        if m != n:
            return False
        for i in range(m):
            ch_map[s[i]] += 1
            ch_map[t[i]] -= 1

        for i in range(26):
            c = chr(ord('a') + i)
            if ch_map[c] != 0:
                return False
        return True
        
        