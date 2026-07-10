class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union Find
        # Path Compression, Union by Rank
        # edges = [[1,2],[1,3],[3,4],[2,4]]
        # edges: 4; nodes: 4
        n = len(edges)
        par = [i for i in range(n + 1)] # ith node -> parent (1 - n)
        rank = [1] * (n + 1)

        def find(n):
            p = par[n]
            if p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]: # remember it's []
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]