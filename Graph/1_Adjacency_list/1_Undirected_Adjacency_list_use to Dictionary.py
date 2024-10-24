class Graph:
    def __init__(self):
        self.adj_list = {}

    # Add an edge to the graph
    def add_edge(self, u, v):
        # Add v to u's adjacency list
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

        # Add u to v's adjacency list (since it's undirected)
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[v].append(u)

    # Print the adjacency list
    def print_graph(self):
        for node in self.adj_list:
            print(f"{node}: {self.adj_list[node]}")

# Example Usage:
graph = Graph()
graph.add_edge(1, 2)   # 1 <<------->> 2
graph.add_edge(1, 3)    # 1 <<------->> 5
graph.add_edge(2, 3)     # 2 <<------->> 3
graph.add_edge(2, 4)     # 2 <<------->> 4


# adjacency list
print(graph.adj_list)

#viw All vertex connection
graph.print_graph()
