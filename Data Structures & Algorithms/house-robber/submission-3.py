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

        prev1 = prev2 = 0
        for i in range(len(nums)):
            cur = max(prev1, prev2 + nums[i])
            prev1, prev2 = cur, prev1
        
        return prev1


        