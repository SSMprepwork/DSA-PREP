class Graph:
    def __init__(self):
        self.graph={}
        self.directed=False

    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def addEdge(self,src,dest):
        self.addVertex(src)
        self.addVertex(dest)

        self.graph[src].append(dest)

        if not self.directed:
            self.graph[dest].append(src)

    def displayGraph(self):
        for vertex in self.graph:
            print(f"{vertex}-->{self.graph[vertex]}")

    def bfs(self, startVertex):
        queue = [startVertex]
        is_visited = [startVertex]
        n=self.graph[startVertex]
        while queue:
            currentVertex = queue.pop()
            print(currentVertex , end = " ")

            for neighbour in self.graph[currentVertex]:
                if neighbour not in is_visited:
                    queue.append(neighbour)
                    is_visited.append(neighbour)

    
    def dfs(self,vertex,visited):
        if vertex not in visited:
            print(vertex,end= " ")
            visited.append(vertex)
            for v in self.graph[vertex]:
                self.dfs(v,visited)

    

G=Graph()
G.addEdge('A','B')
G.addEdge('A','C')
G.addEdge('A','D')
G.addEdge('B','D')
G.addEdge('C','D')
G.addEdge('C','F')
G.addEdge('D','E')
G.addEdge('E','F')

G.displayGraph()
G.bfs("A")



