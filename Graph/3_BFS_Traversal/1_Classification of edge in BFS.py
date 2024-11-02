from collections import deque, defaultdict


def bfs_classification(graph, start):
    visited = set()
    queue = deque([start])
    tree_edges = []
    forward_edges = []
    back_edges = []
    cross_edges = []

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                tree_edges.append((vertex, neighbor))  # Tree edge
            elif (neighbor, vertex) not in tree_edges:
                if (vertex, neighbor) in graph[neighbor]:  # Check for forward edge
                    forward_edges.append((vertex, neighbor))
                else:  # Cross edge or back edge
                    cross_edges.append((vertex, neighbor))  # Assume cross edge for simplicity

    return tree_edges, forward_edges, back_edges, cross_edges


def dfs_classification(graph, vertex, visited, parent):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            print(f"Tree edge: ({vertex}, {neighbor})")
            dfs_classification(graph, neighbor, visited, vertex)
        elif neighbor != parent:
            if neighbor in visited:
                print(f"Back edge: ({vertex}, {neighbor})")  # Cycle detected
            else:
                print(f"Cross edge: ({vertex}, {neighbor})")


# Example directed graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['B'],  # Back edge
    'E': ['C'],  # Cross edge
    'F': []
}

# BFS classification
start_vertex = 'A'
tree_edges, forward_edges, back_edges, cross_edges = bfs_classification(graph, start_vertex)
print("BFS Classification:")
print("Tree Edges:", tree_edges)
print("Forward Edges:", forward_edges)
print("Back Edges:", back_edges)
print("Cross Edges:", cross_edges)

# DFS classification
print("\nDFS Classification:")
visited = set()
dfs_classification(graph, start_vertex, visited, None)
