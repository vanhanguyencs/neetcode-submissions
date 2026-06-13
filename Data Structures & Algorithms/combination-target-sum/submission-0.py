class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        def backtrack(lis, remain, idx):
            if remain == 0:
                ans.append(lis[:])
            if remain < 0:
                return
            for i in range(idx, n):
                lis.append(nums[i])
                backtrack(lis, remain - nums[i], i)
                lis.pop()
        backtrack([], target, 0)
        return ans