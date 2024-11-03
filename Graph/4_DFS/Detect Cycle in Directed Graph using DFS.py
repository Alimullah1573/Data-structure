class Graph:
    def __init__(self, vertices):
        self.graph = [[] for _ in range(vertices)]  # adjacency list representation
        self.V = vertices  # number of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)  # directed graph

    def is_cyclic_util(self, v, visited, rec_stack):
        # Mark the current node as visited and add it to the recursion stack
        visited[v] = True
        rec_stack[v] = True

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            # If the adjacent node is not visited, recur for it
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            # If the adjacent node is in the recursion stack, then a cycle exists
            elif rec_stack[neighbor]:
                return True

        # Remove the vertex from recursion stack
        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.V  # To keep track of visited nodes
        rec_stack = [False] * self.V  # To keep track of nodes in the current recursion stack

        for node in range(self.V):
            # If the node hasn't been visited, check for cycles starting from this node
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False


# Create a directed graph with 5 nodes
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)  # This introduces a cycle

print("Graph contains cycle" if g.is_cyclic() else "Graph doesn't contain cycle")
