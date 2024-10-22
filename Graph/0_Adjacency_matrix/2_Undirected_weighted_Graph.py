
class Graph:
    def __init__(self, vertices):
        # Initialize the number of vertices and the adjacency matrix
        self.V = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v,w):
        # Add an edge (u, v) to the graph
        self.adj_matrix[u][v] = w
        self.adj_matrix[v][u] = w
  #  the graph is uddirected

    def display(self):
        # Print the adjacency matrix
        for row in self.adj_matrix:
            print(row)

# Example usage
if __name__ == "__main__":
    g = Graph(5)  # Create a graph with 5 vertices
    g.add_edge(0, 1,5)           # ( 0<---_5_---->1 )
    g.add_edge(0, 4,10)          # ( 0<---_10_--->4 )
    g.add_edge(1, 2,7)           # ( 1<---_7_---->2 )
    g.add_edge(1, 3,8)           # ( 1<---_8_---->3 )
    g.add_edge(1, 4,9)           # ( 1<---_9_---->4 )
    g.add_edge(2, 3,10)          # ( 2<---_10_---->3 )
    g.add_edge(3, 4,12)          # ( 3<---_12_--->4 )



    # Display the adjacency matrix
    g.display()
