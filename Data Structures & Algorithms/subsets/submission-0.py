class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def backtrack(cur_list, cur_idx):
            ans.append(cur_list[:])
            for i in range(cur_idx, n):
                cur_list.append(nums[i])
                backtrack(cur_list, i + 1)
                cur_list.remove(nums[i])
        
        backtrack([], 0)
        return ans