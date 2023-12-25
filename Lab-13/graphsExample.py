class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.graph = {} # Adjacency list for contacts
        self.weights = {}   # Weights for edges
        self.favorites = {}  # New attribute for storing favorites

   
    #     
    def AddContact(self, username, name, number):
             
              
              if username not in self.nodes: # if userName is not already in the list of nodes 
                  self.nodes.append(username)  # add userName to the list of nodes
                  self.graph[username] = []  # initialize an empty adjacency list for userName in the graph
                  self.favorites[username] = set()  # Initialize favorites as an empty set
          
              if name not in self.nodes:
                  self.nodes.append(name)
                  self.graph[name] = []
              
              if number not in self.nodes:
                  self.nodes.append(number)
                  self.graph[number] = []
          
              # Connect UserName to Name and Contact in the graph
              self.graph[username].append(name)
              self.graph[username].append(number)
              self.graph[name].append(username)
              self.graph[number].append(username)

              # If you have weights associated with edges, initialize them
              self.weights[(username, name)] = 1
              self.weights[(username, number)] = 1
              self.weights[(name, username)] = 1
              self.weights[(number, username)] = 1


    def AddToFavourites(self, username, contact_name):
        if username in self.favorites and contact_name in self.graph[username]:
            self.favorites[username].add(contact_name)


    def PrintGraph(self):
        for node in self.nodes:
            print(self.graph[node])

    def PrintFavourites(self):
        for node in self.nodes:
            print(f"{node}: {self.graph[node]} ")
            if node in self.favorites:
                print(f"Favorites: {self.favorites[node]}")
        
# Example usage
graph = Graph()
graph.AddContact('Hamza', 'Haider', '1234567890')
graph.AddContact('Hamza', 'Kami', '9876543210')
graph.AddContact('Hamza', 'Ali', '1112223333')
graph.AddContact('Hamza', 'Mudasir', '4445556666')

graph.AddContact('Farjad', 'Nomi', '1112223333')
graph.AddContact('Farjad', 'Salman', '4445556666')
graph.AddContact('Farjad', 'Bilal', '7778889999')
graph.AddContact('Farjad', 'amir', '9876543210')

# Add contacts to favorites
graph.AddToFavourites('Hamza', 'Haider')
graph.AddToFavourites('Hamza', 'Kami')
graph.AddToFavourites('Hamza', 'amir')
graph.AddToFavourites('Hamza', 'Ali')

graph.AddToFavourites('Farjad', 'Nomi')
graph.AddToFavourites('Farjad', 'Salman')

# Print the graph with favorites
# graph.PrintGraph()
graph.PrintFavourites()




