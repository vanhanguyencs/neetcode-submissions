class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        There are 2 choices: rob, not rob
        """

        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # dp = [0] * (n + 1)
        # dp[1] = nums[0]
        
        # for i in range (2, n + 1):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        # return dp[n]

        n = len(nums)
        prev2 = 0
        prev1 = 0
        for i in range(0, n):
            cur = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = cur
        
        return prev1


        