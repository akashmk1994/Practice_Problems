from collections import defaultdict


# ----------------------------------------------------------------
# Breadth First Search - Graph Algorithm
# ----------------------------------------------------------------
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BSF(self, s):
        #Mark all vertices as not visited
        visited = [False] * (len(self.graph))
        #Create an empty queue
        queue = []
        #Append node to queue
        queue.append(s)
        #mark node as visiteed
        visited[s] = True
        #check if queue is empty or not
        while queue:
            #print the first value of queue
            s = queue.pop(0)
            print(s, end=" ")
            #check the adjacent node(s) in graph
            for i in self.graph[s]:
                #if not visited then append to queue
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.BSF(2)