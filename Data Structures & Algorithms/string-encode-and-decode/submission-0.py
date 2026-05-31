class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[i] != "#":
                i += 1
            size = int(s[j:i])
            i += 1
            ans.append(s[i: i + size])
            i += size
        return ans

