# def palindrome(s):
#   if(len(s) == 0):
#     return True
#   i = 0
#   if(s[i] == s[len(s)-1]):
#     i+=1
#     return palindrome(s[1:-1])
#   else:
#     return False

# print(palindrome("racecar"))





from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)   #This line appends vertex v to the list of vertices adjacent to vertex u
        self.graph[v].append(u)  

    def bfs(self, start):
        visited = []

        queue = []
        result = []
        queue.append(start)
        visited.append(start)

        while len(queue) > 0:
            vertex = queue.pop()

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)
                    result.append(neighbor)

        return result

    def DFS(self,root):
        visited = []
        stack = []
        stack.append(root)
        visited.append(root)
        print("root:",root,end=" ")
        while(stack):
            root = stack.pop()
            for neighour in self.graph[root]:
                if neighour not in visited:
                    stack.append(neighour)
                    visited.append(neighour)
                    print("-->",neighour,end=" ")
        

    


my_graph = Graph()

my_graph.add_edge(5,2)
my_graph.add_edge(5,1)
my_graph.add_edge(1,3)
my_graph.add_edge(2,0)
my_graph.add_edge(0,7)
my_graph.add_edge(0,6)
my_graph.add_edge(6,7)

start_vertex = 5
bfs_result = my_graph.bfs(start_vertex)

print("DFS starting from vertex 5: ")
dfs = my_graph.DFS(start_vertex)


print("\n")
print(f"BFS starting from vertex {start_vertex}: {bfs_result}")





##########    RB TREE   ##############
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.parent = None
#         self.left = None
#         self.right = None
#         self.color = 'red'



# class RBTree:
#     def __init__(self):
#         self.NIL = Node(None, 'black')
#         self.root = self.NIL


#     def insert(self, value):
#         node = Node(value)
#         node.parent = None

#         node.left = self.NIL

#         node.right = self.NIL
#         node.color = 'red'



#         y = None
#         x = self.root

#         while x != self.NIL:
#             y = x

                