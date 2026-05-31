class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, cnt in count_map.items():
            freq[cnt].append(num)
        
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans