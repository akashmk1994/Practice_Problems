from collections import defaultdict


# ----------------------------------------------------------------
# Connected Graph Algorithm
# ----------------------------------------------------------------
# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
#
#     def edge_add(self, u, v):
#         self.graph[u].append(v)
#
#     def utild(self, v, visited):
#         visited[v] = True
#         print(v, end='')
#         for i in self.graph[v]:
#             if visited[i]==False:
#                 self.utild(i, visited)
#
#     def DFS(self,v):
#         #Mark all as not visited
#         visited = [False]*(max(self.graph)+1)
#         self.utild(v, visited)
# ----------------------------------------------------------------------
# Disconnected Graph Algorithm
# ----------------------------------------------------------------
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def edge_add(self, u, v):
        self.graph[u].append(v)

    def util(self, v, visited):
        visited[v] = True
        print(v, end='')
        for i in self.graph[v]:
            if visited[i] == False:
                self.util(i, visited)

    def DFSC(self):
        # Length of the Graph
        ver = len(self.graph)
        # Mark all as not visited
        visited = [False] * (ver)
        # Traverse all nodes one by one
        for i in range(ver):
            if visited[i] == False:
                self.util(i, visited)


obj = Graph()
obj.edge_add(0, 1)
obj.edge_add(0, 2)
obj.edge_add(1, 2)
obj.edge_add(2, 0)
obj.edge_add(2, 3)
obj.edge_add(3, 3)
#obj.DFS(2) #Connected Graph - Specify node from where to start and traverse nodes
obj.DFSC()  # Disconnected Graph - Dont specify, Autodetect not visited
