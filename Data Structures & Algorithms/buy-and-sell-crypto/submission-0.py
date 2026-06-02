class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_so_far = prices[0]
        for p in prices:
            ans = max(ans, p - min_so_far)
            min_so_far = min(min_so_far, p)
        return ans