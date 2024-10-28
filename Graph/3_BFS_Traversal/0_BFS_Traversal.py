# Function to perform BFS
def BFS(graph, start_node):
    visited = []
    queue = []
    queue.append(start_node)
    visited.append(start_node)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for child in graph[node]:
            if child not in visited:
                queue.append(child)
                visited.append(child)


# Function to create the graph
def create_graph(total_vertex):
    graph = {}
    for _ in range(total_vertex):
        vertex = input("Enter vertex: ")
        graph[vertex] = []

        while True:
            child = input("Enter child vertex (or -1 to stop): ")
            if child == '-1':
                break
            graph[vertex].append(child)
    return graph


# Main code
total_vertex = int(input("Enter the number of vertices: "))
graph = create_graph(total_vertex)
print("Graph:", graph)

# Run BFS if graph is not empty
if graph:
    start_vertex = input("Enter starting vertex for BFS: ")
    BFS(graph, start_vertex)
else:
    print("The graph is empty.")
