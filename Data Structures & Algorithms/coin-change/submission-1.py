from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(amount):
            if amount == 0:
                return 0
            ans = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    ans = min(ans, 1 + dfs(amount - coin))
            return ans
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins