class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n:
            return False
        arr = [0] * 26
        for i in range(m):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1
        
        for a in arr:
            if a != 0:
                return False
        return True