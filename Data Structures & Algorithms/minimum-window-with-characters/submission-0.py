class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(t)
        if len(s) < len(t):
            return ""

        countT = Counter(t)

        ans = ""
        ansLen = float("inf")
        need = len(countT)

        have = 0

        l = 0
        window = {}
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < ansLen:
                    ansLen = r - l + 1
                    ans = s[l:r + 1]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return ans

