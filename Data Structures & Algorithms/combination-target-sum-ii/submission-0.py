class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()

        def backtrack(lis, total, idx):
            if total == target:
                ans.append(lis[:])
            if idx >= n or total + candidates[idx] > target:
                return
            
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                lis.append(candidates[i])
                backtrack(lis, total + candidates[i], i + 1)
                lis.pop()
        backtrack([], 0, 0)
        return ans