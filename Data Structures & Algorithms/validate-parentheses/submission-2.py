class Solution:
    def isValid(self, s: str) -> bool:
        look_up = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for c in s:
            if c not in look_up.keys():
                stack.append(c)
            else:
                if not stack or look_up[c] != stack[-1]:
                    return False
                stack.pop()
        return not stack
                