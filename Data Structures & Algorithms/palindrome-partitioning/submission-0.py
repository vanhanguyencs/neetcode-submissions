class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(sub):
            l, r = 0, len(sub) - 1
            while l < r:
                if sub[l] != sub[r]:
                    return False
                l += 1
                r -= 1
            return True
        ans = []
        n = len(s)
        if s == "":
            return [[]]
        for i in range(n):
            prefix = s[:(i + 1)]
            if isPalin(prefix):
                for p in self.partition(s[i+ 1:]):
                    ans.append([prefix] + p)
        return ans