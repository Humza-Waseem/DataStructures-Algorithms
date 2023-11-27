#####################   This makes the copies of the same items in the list so when we append, the same item is appended to all the lists   #####################
# array = [[] ] * 5
# array[0].append(5)
# print(array)


##################### This doesn't make the copies , and appending an item in the list, doesn't append it to all the lists   #####################
# array = [[] for i in range(5)]
# array[0].append(5)
# print(array) 


# class Graph:
#     def __init__(self, numOfVertices, edges):
#         self.numOfVertices = numOfVertices
#         self.data = [[] for i in range(numOfVertices)]
#         for edge in edges:
#             self.addEdge(edge[0], edge[1])


#     def addEdge(self, u, v):
#         self.data[u].append(v)
#         self.data[v].append(u)

#     def printGraph(self):
#         for i in range(len(self.data)):
#             print(i, ":", self.data[i])

#     def bfs(self, root):
#         queue = []
#         discovered = [False] * len(self.data)
#         distance = [None] * len(self.data)
#         parent = [None] * len(self.data)

#         discovered[root] = True
#         queue.append(root)
#         distance[root] = 0
#         idx = 0

#         while idx < len(queue):
#             current = queue[idx]
#             idx += 1
#             for neighbor in self.data[current]:
#                 if not discovered[neighbor]:
#                     discovered[neighbor] = True
#                     queue.append(neighbor)
#                     distance[neighbor] = distance[current] + 1
#                     parent[neighbor] = current
#         print("QUeue:")
#         print(queue)
#         print("Discovered:")
#         print(discovered)
#         print("Distance:")
#         print(distance)
#         print("Parent:")
#         print(parent)


# graph = Graph(5, [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)])
# graph.printGraph()
# graph.bfs(0)

# queue = []
# discovered = [False] * len(graph.data)
# distance = [None] * len(graph.data)
# parent = [None] * len(graph.data)

# discovered[root] = True
# queue.append(root)
# distance[root] = 0
# idx = 0

# while idx < len(queue):
#     current = queue[idx]
#     idx += 1
#     for neighbor in graph.data[current]:
#         if not discovered[neighbor]:
#             discovered[neighbor] = True
#             queue.append(neighbor)
#             distance[neighbor] = distance[current] + 1
#             parent[neighbor] = current

# print(queue)
# print(discovered)
# print(distance)
# print(parent)


# numOfVertices = 5
# edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
# print((edges))





# class Graph:
#     def __init__(self, num_of_vertices):
#         self.num_of_vertices = num_of_vertices
#         self.adjacency_list = {i: [] for i in range(self.num_of_vertices)}

#     def add_edge(self, u, v):
#         self.adjacency_list[u].append(v)
#         self.adjacency_list[v].append(u)

#     def dfs(self, start_vertex):
#         visited = [False for _ in range(self.num_of_vertices)]
#         self.dfs_util(start_vertex, visited)

#     def dfs_util(self, vertex, visited):
#         visited[vertex] = True
#         print(vertex, end=' ')

#         for neighbor in self.adjacency_list[vertex]:
#             if not visited[neighbor]:
#                 self.dfs_util(neighbor, visited)



# graph = Graph(5)
# graph.add_edge(0, 1)
# graph.add_edge(0, 4)
# graph.add_edge(1, 2)
# graph.add_edge(1, 3)
# graph.add_edge(1, 4)
# graph.add_edge(2, 3)
# graph.add_edge(3, 4)
# graph.dfs(0)
# print(graph.adjacency_list)




        


