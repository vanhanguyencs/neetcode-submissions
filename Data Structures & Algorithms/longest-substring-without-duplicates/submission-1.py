class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_map = defaultdict(int)
        l = 0
        ans = 0
        for r in range(len(s)):
            c = s[r]
            ch_map[c] += 1
            while ch_map[c] > 1:
                ch_map[s[l]] -= 1
                l += 1
            ans = max(ans, (r - l + 1))
        return ans
