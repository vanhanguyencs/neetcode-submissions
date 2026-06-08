class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        1 2 3 2 2
        num in nums:
            idx = num - 1
            if nums[idx] < 0:
                duplicate
                return nums[idx]??
            nums[idx] *= -1
        
        -1 -2 -3 2 2

        -1 -2 -3 -4 4


        -1 -3 -4 -2 2

        """
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        
        return -1