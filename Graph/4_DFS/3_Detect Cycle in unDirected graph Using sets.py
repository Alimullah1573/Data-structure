class DisjointSet:
    def __init__(self, n):
        # Initialize parent and rank arrays
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        # Path compression optimization
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            # Union by rank optimization
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
            return False  # No cycle formed
        return True  # Cycle detected


def detect_cycle(edges, n):
    ds = DisjointSet(n)
    for u, v in edges:
        if ds.union(u, v):
            return True  # Cycle detected
    return False  # No cycle

# Example usage
edges = [(0, 1), (1, 2), (2, 0)]  # Example with a cycle
n = 3  # Number of nodes
print("Cycle Detected" if detect_cycle(edges, n) else "No Cycle Detected")
