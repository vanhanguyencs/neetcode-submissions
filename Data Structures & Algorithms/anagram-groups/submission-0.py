class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        look_up = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in look_up:
                look_up[key].append(s)
            else:
                look_up[key] = [s]
        
        ans = []
        for key in look_up:
            ans.append(look_up[key])
        return ans
