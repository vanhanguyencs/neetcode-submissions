class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        BFS
        """
        # build graph
        graph = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)

        q = deque()
        q.append((0, -1))
        visited = set()
        while q:
            node, parent = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                q.append((nei, node))
        return len(visited) == n




