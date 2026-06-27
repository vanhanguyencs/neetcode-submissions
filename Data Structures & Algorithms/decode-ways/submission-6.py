from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        # @cache
        # def dfs(i):
        #     if i == len(s):
        #         return 1
        #     if s[i] == '0':
        #         return 0
            
        #     ans = dfs(i + 1)
        #     if i < (len(s) - 1) and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
        #         ans += dfs(i + 2)
        #     return ans
        # return dfs(0)
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                dp[i] += dp[i + 2]
        return dp[0]