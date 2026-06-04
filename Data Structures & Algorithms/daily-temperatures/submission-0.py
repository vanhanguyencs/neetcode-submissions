class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        stack = [] # temp, index

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, idx = stack.pop()
                ans[idx] = i - idx
            stack.append((temp, i))
        
        return ans
