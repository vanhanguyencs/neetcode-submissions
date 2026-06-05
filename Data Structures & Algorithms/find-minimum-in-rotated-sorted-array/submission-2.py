class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if n == 1 or nums[0] < nums[n - 1]:
            return nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l + r) // 2
            # min number i is detected by nums[i - 1] > nums[i]
            print(f'left: {l} right: {r}, mid = {mid}')
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] >= nums[l]: #left part is sorted
                l = mid + 1
            else:
                r = mid - 1
        
        return nums[mid]