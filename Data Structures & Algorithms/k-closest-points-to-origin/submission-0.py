from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        max heap
        """

        pq = []
        for p in points:
            square = p[0]*p[0] + p[1]*p[1]
            heappush(pq, (-square, p[0], p[1]))

            while len(pq) > k:
                heappop(pq)
        
        ans = []
        while pq:
            _, x, y = heappop(pq)
            ans.append([x, y])
        return ans

            