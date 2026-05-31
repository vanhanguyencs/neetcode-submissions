class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        val_to_idx = {}
        for i, num in enumerate(numbers):
            remain = target - num
            if remain in val_to_idx.keys():
                return [val_to_idx[remain] + 1, i + 1]
            val_to_idx[num] = i
        
        return [-1, -1]