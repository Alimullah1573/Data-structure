from collections import defaultdict

# Define a Graph class
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Adjacency list representation of the graph
        self.V = vertices  # Number of nodes
        self.time = 0  # Time tracker for discovery and finishing times

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Function to classify edges using DFS traversal
    def dfs_classification(self):
        # Arrays to keep track of each node's state
        visited = [False] * self.V
        discovery = [-1] * self.V  # Discovery time of nodes
        finish = [-1] * self.V  # Finish time of nodes

        # Loop to start DFS traversal from each unvisited node
        for u in range(self.V):
            if not visited[u]:
                self.dfs_visit(u, visited, discovery, finish)

    # Helper function to perform DFS and classify edges
    def dfs_visit(self, u, visited, discovery, finish):
        visited[u] = True
        self.time += 1
        discovery[u] = self.time

        for v in self.graph[u]:
            # Tree Edge: Edge leading to an unvisited node
            if not visited[v]:
                print(f"Tree Edge: ({u} -> {v})")
                self.dfs_visit(v, visited, discovery, finish)
            # Back Edge: Edge leading to an ancestor in the DFS tree
            elif discovery[u] > discovery[v] and finish[v] == -1:
                print(f"Back Edge: ({u} -> {v})")
            # Forward Edge: Edge leading to a descendant not in the DFS tree
            elif discovery[u] < discovery[v]:
                print(f"Forward Edge: ({u} -> {v})")
            # Cross Edge: Edge connecting two nodes in different branches
            else:
                print(f"Cross Edge: ({u} -> {v})")

        # Mark the finish time of the node
        self.time += 1
        finish[u] = self.time

# Create a graph instance
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Print edge classification in the graph
print("Edge Classification in the graph:")
g.dfs_classification()
