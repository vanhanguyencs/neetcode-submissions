class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()

        def backtrack(path: List[int], total: int, start: int) -> None:
            if total == target:
                ans.append(path[:])
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                new_total = total + candidates[i]
                if new_total > target:
                    break
                path.append(candidates[i])
                backtrack(path, new_total, i + 1)
                path.pop()
        backtrack([], 0, 0)
        return ans