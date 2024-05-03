import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    
    def prims_mst(self):
        
        # Initialize minimum spanning tree
        mst = []
        
        # Initialize priority queue and visited set
        pq = [(0, None, list(self.graph.keys())[0])]  # (weight, parent, node)
        visited = set()
        
        # Main Prim's algorithm loop
        while pq:
            weight, parent, node = heapq.heappop(pq)
            
            # If the node has already been visited, skip it
            if node in visited:
                continue
            
            # Mark the node as visited
            visited.add(node)
            
            # If this is not the first node, add the edge to the MST
            if parent is not None:
                mst.append((parent, node, weight))
            
            # Add adjacent nodes to the priority queue
            for neighbors, weight in self.graph[node]:
                if neighbors not in visited:
                    heapq.heappush(pq, (weight, node, neighbors))
        
        return mst

# Example usage:
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

# Compute MST
mst = g.prims_mst()

# Print MST
print("Minimum Spanning Tree (MST):")
for edge in mst:
    print(edge)