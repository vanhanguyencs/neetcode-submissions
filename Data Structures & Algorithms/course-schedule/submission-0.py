class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        DFS or BFS

        """

        # build graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for p in prerequisites:
            u, v = p[0], p[1]
            graph[v].append(u)
            indegree[u] += 1
        
        q = deque()
        finish = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                finish += 1
        
        while q:
            node = q.popleft()
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    finish += 1
        
        return finish == numCourses



        