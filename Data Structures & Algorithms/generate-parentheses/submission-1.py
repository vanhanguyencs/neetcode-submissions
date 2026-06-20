class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        just generate for string 2*n len
        then check if the parentheses is valid


        """
        def isValid(s) -> bool:
            bal = 0
            for ch in s:
                bal += 1 if ch == '(' else -1
                if bal < 0:
                    return False
            return not bal
        
        ans = []
        def dfs(s):
            if len(s) == 2*n:
                if isValid(s):
                    ans.append(s)
                return
            dfs(s + '(')
            dfs(s + ')')
        dfs("")
        return ans
