
class Graph:
    def __init__(self, vertices):
        # Initialize the number of vertices and the adjacency matrix
        self.V = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        # Add an edge (u, v) to the graph
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # Since the graph is undirected

    def display(self):
        # Print the adjacency matrix
        for row in self.adj_matrix:
            print(row)

# Example usage
if __name__ == "__main__":
    g = Graph(5)  # Create a graph with 5 vertices
    g.add_edge(0, 1)           # ( 0<-------->1 )
    g.add_edge(0, 4)           # ( 0<------->4 )
    g.add_edge(1, 2)           # ( 1<------->2 )
    g.add_edge(1, 3)           # ( 1<------->3 )
    g.add_edge(1, 4)           # ( 1<------->4 )
    g.add_edge(2, 3)           # ( 2<------->3 )
    g.add_edge(3, 4)           # ( 3<------->4 )



    # Display the adjacency matrix
    g.display()
