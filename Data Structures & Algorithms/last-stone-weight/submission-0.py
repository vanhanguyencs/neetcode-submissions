from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        using max heap
        """
        pq = []
        for stone in stones:
            heappush(pq, -stone)
        
        while len(pq) > 1:
            a = -heappop(pq)
            b = -heappop(pq)
            if a == b:
                continue
            heappush(pq, -abs(a - b))
        return -pq[0] if len(pq) > 0 else 0