class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for p, s in cars:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)

        """ 

        position= [0, 7]
        speed = [10, 1]
        target = 10

        position  speed  time
        7         1      3
        0         10     1

        stack[]
        so the car at position 7 is slower take 3 hours
        and the car behind at position 0 need to wait
        so the result is only 1 fleet.
        """
