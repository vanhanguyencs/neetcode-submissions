class Solution:
    def countSubstrings(self, s: str) -> int:
        def extendPalindrome(start, end):
            nonlocal ans
            while start >= 0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1
                ans += 1
        
        ans = 0
        n = len(s)
        for i in range(n):
            extendPalindrome(i, i)
            if i < n - 1 and s[i] == s[i + 1]:
                extendPalindrome(i, i + 1)
        return ans
            
            