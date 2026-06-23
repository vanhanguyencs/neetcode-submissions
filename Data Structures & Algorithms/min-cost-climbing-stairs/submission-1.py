class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        min_so_far
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = cost[0]
        dp[2] = min(dp[1], dp[0] + cost[1])
        # not take 2: dp[1]
        # take 2: dp[0] + cost[1]
        # wrong
        dp[3] = min(dp[2], dp[1] + cost[2])
        # not take 3: dp[0] + cost[1] must take previous one
        # take 3: dp[1] + cost[2]
        """
        n = len(cost)
        dp = [0] * (n + 1)
        a, b = 0, 0
        for i in range(2, n + 1):
            not_take = a + cost[i - 2]
            take = b + cost[i - 1]
            c = min(not_take, take)
            a = b
            b = c
        return b
