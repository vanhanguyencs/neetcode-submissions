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
        def rob_linear(start: int, end: int) -> int:
            prev1 = prev2 = 0
            for i in range(start, end):
                cur = max(prev1, prev2 + nums[i])
                prev1, prev2 = cur, prev1
            return prev1
        n = len(nums)
        if n == 1:
            return nums[0]
        return max (
            rob_linear(0, n - 1), # exclude the last house
            rob_linear(1, n)    # exclude the first house
        )
