


class Graph:
    def __init__(self, vertices):
        self.graph = [[] for _ in range(vertices)]  # adjacency list representation
        self.V = vertices  # number of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # undirected graph

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True  # mark current node as visited

        for neighbor in self.graph[v]:
            # if neighbor hasn't been visited, recursively visit it
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, v):  # pass current node as parent
                    return True
            # if neighbor is visited and not parent of current node, then cycle exists
            elif neighbor != parent:
                return True

        return False

    def is_cyclic(self):
        visited = [False] * self.V  # to keep track of visited nodes

        for i in range(self.V):
            # if the node hasn't been visited, check for cycles starting from this node
            if not visited[i]:
                if self.is_cyclic_util(i, visited, -1):  # -1 is used as the initial parent
                    return True
        return False


# Create a graph with 5 nodes
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(2, 3)
g.add_edge(1,2)
g.add_edge(0,3)

print("Graph contains cycle" if g.is_cyclic() else "Graph doesn't contain cycle")
