class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_prefix = [0] * n
        max_suffix = [0] * n

        for i in range(1, n):
            max_prefix[i] = max(max_prefix[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            max_suffix[i] = max(max_suffix[i + 1], height[i + 1])
        
        ans = 0
        for i in range(n):
            min_height = min(max_prefix[i], max_suffix[i])
            ans += max(0, min_height - height[i])
        return ans

