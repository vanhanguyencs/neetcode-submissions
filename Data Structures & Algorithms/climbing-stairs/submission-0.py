class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1 -> 1
        2 -> 2
        3 -> 3
        4 -> 5
        """
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return b