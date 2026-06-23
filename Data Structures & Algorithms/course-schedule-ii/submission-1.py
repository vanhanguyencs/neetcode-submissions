class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for p in prerequisites:
            u, v = p[0], p[1]
            graph[v].append(u)
            indegree[u] += 1
        
        q = deque()
        order = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                order.append(i)
        
        while q:
            node = q.popleft()
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    order.append(nei)
        
        return order if len(order) == numCourses else []