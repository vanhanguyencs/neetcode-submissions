from heapq import heapify, heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        count number of each task
        schedule the task with highest count first

        tasks = ["X","X","Y","Y"], n = 2
        X: 2
        Y: 2

        max_heap (X: 2, Y: 2)
        time = 1
        X
        time = 2
        Y
        max_heap (X: 1, Y: 1)
        

        """
        freq = [0] * 26
        for ch in tasks:
            freq[ord(ch) - ord('A')] += 1
        
        pq = [-f for f in freq if f > 0]
        heapify(pq)
        time = 0

        while pq:
            print(time)
            cycle = n + 1
            task_count = 0
            store = []

            while cycle > 0 and pq:
                count = -heappop(pq)
                count -= 1
                print(f'count: {count}')
                if count >= 1:
                    store.append(-count)
                task_count += 1
                cycle -=1
            
            print(f'lenstore: {len(store)}')
            for x in store:
                heappush(pq, x)
            time += task_count if not pq else n + 1
        
        return time

