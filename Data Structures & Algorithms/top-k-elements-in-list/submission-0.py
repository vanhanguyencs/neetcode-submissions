class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        sorted_items = sorted(count_map.items(), key=lambda x: -x[1])
        return [num for num, freq in sorted_items[:k]]
