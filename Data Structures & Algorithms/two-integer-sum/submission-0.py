class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_idx = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in val_to_idx:
                return [val_to_idx[remain], i]
            val_to_idx[num] = i
        
        return {-1, -1}