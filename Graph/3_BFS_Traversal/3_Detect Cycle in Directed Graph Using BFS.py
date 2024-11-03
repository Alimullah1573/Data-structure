class Graph:
    def __init__(self, vertices):
        self.graph = [[] for _ in range(vertices)]  # adjacency list representation
        self.V = vertices  # number of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)  # directed graph: only add u -> v

    def is_cyclic(self):
        # In-degree array to count in-degrees of each vertex
        in_degree = [0] * self.V
        for u in range(self.V):
            for v in self.graph[u]:
                in_degree[v] += 1

        # Queue of vertices with zero in-degree
        queue = [i for i in range(self.V) if in_degree[i] == 0]

        # Count of visited vertices
        count = 0

        while queue:
            node = queue.pop(0)
            count += 1

            # For all neighbors of the current node
            for neighbor in self.graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If count doesn't match the number of vertices, there's a cycle
        return count != self.V

# Create a directed graph with 4 nodes
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(0, 3)

print("Graph contains cycle" if g.is_cyclic() else "Graph doesn't contain cycle")
