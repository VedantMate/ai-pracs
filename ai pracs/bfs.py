from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self,start):

        queue = []
        visited = set()
        queue.append(start)
        visited.add(start)

        while queue:

            vertex = queue.pop(0)
            print(vertex,end =" ")

            for neighbours in self.graph[vertex]:

                if neighbours not in visited:
                    queue.append(neighbours)
                    visited.add(neighbours)

    def dfs(self, start):
        stack = []
        visited = set()
        stack.append(start)

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)

                for neighbour in reversed(self.graph[vertex]):
                    if neighbour not in visited:
                        stack.append(neighbour)




g = Graph()
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,0)
g.addedge(1,2)
g.addedge(1,3)
g.addedge(2,0)
g.addedge(2,1)
g.addedge(2,4)
g.addedge(3,1)
g.addedge(3,4)
g.addedge(4,3)
g.addedge(4,2)

g.bfs(0)
print("/n")
g.dfs(0)