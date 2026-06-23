class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort by the start
        iterate
        """

        intervals.sort(key=lambda x: x[0])

        n = len(intervals)
        ans = []
        i = 0
        while i < n:
            print(f'i = {i} ans: {ans}')
            if i == n - 1 or intervals[i][1] < intervals[i + 1][0]:
                print("aa")
                ans.append(intervals[i])
                i += 1
            else:
                a, b = intervals[i][0], intervals[i][1]
                print(f'a = {a} b = {b}')
                i += 1
                while i < n and intervals[i][0] <= b :
                    a = min(a, intervals[i][0])
                    b = max(b, intervals[i][1])
                    i += 1
                ans.append([a, b])
        
        return ans
            



