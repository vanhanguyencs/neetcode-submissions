class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        just generate for string 2*n len
        then check if the parentheses is valid


        """
        def isValid(s) -> bool:
            bal = 0
            for ch in s:
                if ch == '(':
                    bal += 1
                else:
                    if bal == 0:
                        return False
                    bal -= 1
            return bal == 0
        
        ans = []
        def dfs(s):
            if len(s) == 2*n:
                if isValid(s):
                    ans.append(s)
                return
            s += '('
            dfs(s)
            s = s[:-1]
            
            s += ')'
            dfs(s)
            s = s[:-1]
        dfs("")
        return ans
