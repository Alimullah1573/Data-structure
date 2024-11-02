class Graph:
    def __init__(self, vertices):
        self.graph = [[] for _ in range(vertices)]  # adjacency list representation
        self.V = vertices  # number of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # undirected graph

    def is_cyclic(self):
        visited = [False] * self.V  # to keep track of visited nodes

        # Perform BFS from each unvisited node
        for i in range(self.V):
            if not visited[i]:
                if self.is_cyclic_bfs(i, visited):
                    return True
        return False

    def is_cyclic_bfs(self, start, visited):
        # Using a list as a queue
        queue = [(start, -1)]
        visited[start] = True

        while queue:
            v, parent = queue.pop(0)  # Pop the first element to simulate queue behavior

            for neighbor in self.graph[v]:
                # If neighbor hasn't been visited, add it to the queue
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, v))
                # If visited and not parent, cycle exists
                elif neighbor != parent:
                    return True

        return False


# Create a graph with 5 nodes
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(2, 3)
g.add_edge(1, 2)
g.add_edge(0, 3)

print("Graph contains cycle" if g.is_cyclic() else "Graph doesn't contain cycle")
