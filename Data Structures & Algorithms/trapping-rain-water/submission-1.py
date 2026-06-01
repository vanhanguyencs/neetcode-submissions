class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_prefix = [0] * n
        max_suffix = [0] * n

        max_prefix[0] = height[0]
        for i in range(1, n):
            max_prefix[i] = max(max_prefix[i - 1], height[i])
        
        max_suffix[n- 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_suffix[i] = max(max_suffix[i + 1], height[i])
        
        ans = 0
        for i in range(n):
            ans += min(max_prefix[i], max_suffix[i]) - height[i]
        return ans

