class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(path, visited):
            if len(path) == n:
                ans.append(path[:])
                return

            for i in range(n):
                if i in visited:
                    continue

                visited.add(i)
                path.append(nums[i])

                backtrack(path, visited)

                path.pop()
                visited.remove(i)

        backtrack([], set())
        return ans