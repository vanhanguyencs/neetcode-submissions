class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)

        ans = r
        while l <= r:
            k = (l + r) // 2
            if k == 0:
                break
            #see if koko can eat all banana in k hours
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                ans = min(ans, k)
                r = k - 1
            else:
                l = k + 1
        return ans
