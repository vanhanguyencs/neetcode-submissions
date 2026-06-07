from collections import defaultdict
from bisect import bisect_right
class TimeMap:
    
    def __init__(self):
        self.lookup = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.lookup[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.lookup[key]
        idx = bisect_right(values, timestamp, key=lambda x: x[1]) - 1
        return values[idx][0] if idx >= 0 else ""
        
