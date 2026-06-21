class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        3 - 0 - 1 - 4
            |
            2 
        DFS
        """
        graph = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
