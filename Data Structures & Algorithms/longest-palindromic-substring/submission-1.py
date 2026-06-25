class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        for each character in string s, extend to left and right
        - two cases:
            + abcba
            + abccba
        time O(n^2)

        """
        def extendPalindrome(l, r):
            while l >= 0 and r <= n - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        n = len(s)
        max_str = ""
        for i in range(n):
            odd = extendPalindrome(i, i)
            if len(odd) > len(max_str):
                max_str = odd
            if i < n - 1 and s[i] == s[i + 1]:
                even = extendPalindrome(i, i + 1)
                if len(even) > len(max_str):
                    max_str = even
        return max_str
