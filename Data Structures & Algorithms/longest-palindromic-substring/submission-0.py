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
            return (r - l - 1, s[l+1:r])
        n = len(s)
        max_len = 0
        max_str = ""
        for i in range(n):
            cur_len, cur_str = extendPalindrome(i, i)
            if cur_len > max_len:
                max_len = cur_len
                max_str = cur_str
            if i < n - 1 and s[i] == s[i + 1]:
                cur_len, cur_str = extendPalindrome(i, i + 1)
                if cur_len > max_len:
                    max_len = cur_len
                    max_str = cur_str
        return max_str
