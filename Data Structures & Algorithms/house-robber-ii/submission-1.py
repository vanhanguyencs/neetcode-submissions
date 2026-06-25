class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i] = max (
                dp[i - 1], # not take
                dp[i - 2] + nums[i]
                )
        dp[1] vs dp[n]?
        carry if the result take nums[0] or not?

        """
        n = len(nums)
        if n == 1:
            return nums[0]
        prev1 = prev2 = 0
        for i in range(n - 1):
            cur = max(prev1, prev2 + nums[i])
            prev1, prev2 = cur, prev1
        ans = prev1
        prev1 = prev2 = 0
        for i in range(1, n):
            cur = max(prev1, prev2 + nums[i])
            prev1, prev2 = cur, prev1
        
        ans = max(ans, prev1)
        return ans
