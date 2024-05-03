class Graph:

    def __init__(self):
        self.graph = []

    def addedge(self, u, v, w):
        self.graph.append((w, u, v))

    def kruskalMST(self):
        self.graph.sort()  # Sort edges by weight
        parent = {}
        rank = {}
        mst = []
        total_cost = 0

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        for edge in self.graph:
            weight, u, v = edge
            if u not in parent:
                parent[u] = u
                rank[u] = 0
            if v not in parent:
                parent[v] = v
                rank[v] = 0
            if find(u) != find(v):
                mst.append((u, v, weight))
                total_cost += weight
                union(u, v)

        print("Edges in the constructed MST:")
        for u, v, weight in mst:
            print("%s -- %s == %d" % (u, v, weight))
        print("Minimum Spanning Tree Total Cost:", total_cost)



g = Graph()

g.addedge('A','B',1)
g.addedge('A','F',2)
g.addedge('B','C',4)
g.addedge('B','E',2)
g.addedge('E','F',5)
g.addedge('F','G',4)
g.addedge('C','G',3)
g.addedge('C','D',6)
g.addedge('G','D',2)

g.kruskalMST()
