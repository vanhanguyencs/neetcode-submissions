class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] > heights[i]):
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        
        return ans