from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # @cache
        # def dfs(amount):
        #     if amount == 0:
        #         return 0
        #     ans = 1e9
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             ans = min(ans, 1 + dfs(amount - coin))
        #     return ans
        # minCoins = dfs(amount)
        # return -1 if minCoins >= 1e9 else minCoins
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != (amount + 1) else -1
        

