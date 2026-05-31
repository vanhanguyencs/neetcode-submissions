class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        look_up = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            look_up[key].append(s)
        return list(look_up.values())
