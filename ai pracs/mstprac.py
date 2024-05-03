import sys

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, u, v, weight):
        if u not in self.vertices:
            self.vertices[u] = []
        if v not in self.vertices:
            self.vertices[v] = []
        self.vertices[u].append((v, weight))
        self.vertices[v].append((u, weight))

    def prim_mst(self):
        mst = []
        visited = set()
        start_vertex = next(iter(self.vertices)) 
        visited.add(start_vertex)
        while len(visited) < len(self.vertices):
            min_edge = None
            min_weight = sys.maxsize
            for vertex in visited:
                for neighbor, weight in self.vertices[vertex]:
                    if neighbor not in visited and weight < min_weight:
                        min_weight = weight
                        min_edge = (vertex, neighbor, weight)
            if min_edge:
                mst.append(min_edge)
                visited.add(min_edge[1])  
        return mst

g = Graph()
# Add edges to the graph
g.add_edge('A','B',1)
g.add_edge('A','F',2)
g.add_edge('B','C',4)
g.add_edge('B','E',2)
g.add_edge('E','F',5)
g.add_edge('F','G',4)
g.add_edge('C','G',3)
g.add_edge('C','D',6)
g.add_edge('G','D',2)

mst = g.prim_mst()
print("Minimal Spanning Tree:")
for edge in mst:
    print(edge)
