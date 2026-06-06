class TimeMap:
    
    def __init__(self):
        self.look_up = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.look_up[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        tmp_stack = []
        cur_stack = self.look_up[key]
        while cur_stack and timestamp < cur_stack[-1][1]:
            tmp_stack.append(cur_stack.pop())
        
        ans = cur_stack[-1][0] if cur_stack else ""
        
        while tmp_stack:
            cur_stack.append(tmp_stack.pop())

        return ans
        
