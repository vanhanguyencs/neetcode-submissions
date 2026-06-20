class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        1, 2, 1
        sort:
        1, 1, 2
        lis = []
        ans.append(lis)
        lis = 1
        ans.append(lis)
        lis = 1, 1
        ans.append(lis)
        lis = 1, 1, 2

        """
        ans = []
        n = len(nums)
        nums.sort()

        def dfs(lis, idx):
            ans.append(lis[:])

            for i in range(idx, n):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                lis.append(nums[i])
                dfs(lis, i + 1)
                lis.pop()
        
        dfs([], 0)
        return ans