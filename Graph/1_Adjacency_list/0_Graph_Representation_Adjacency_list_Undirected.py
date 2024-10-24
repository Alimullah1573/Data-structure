class Graph:
    def __init__(self, num_of_nodes):
        self.num_of_nodes = num_of_nodes
        self.nodes = list(range(num_of_nodes))  # List of nodes
        self.adj_list = [[] for _ in range(num_of_nodes)]  # Adjacency list initialized with empty lists

    # Add an edge to the graph
    def add_edge(self, node, neighbor):                 
        self.adj_list[node].append(neighbor)
        self.adj_list[neighbor].append(node)

    # Print the adjacency list
    def print_graph(self):
        for node in self.nodes:
            print(f"{node} -> {self.adj_list[node]}")

# Create a graph with 4 nodes
g = Graph(4)
g.add_edge(0, 1)   # 0 -> [1]
g.add_edge(0, 2)  # 0 -> [1, 2]
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Print the adjacency list
g.print_graph()
