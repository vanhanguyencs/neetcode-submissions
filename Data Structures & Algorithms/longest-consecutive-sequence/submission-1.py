class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        store = set(nums)

        for num in nums:
            if (num - 1) in store:
                continue
            length = 1
            while (num + length) in store:
                length += 1
            ans = max(ans, length)
        return ans