# Function to perform BFS on a graph
def BFS(graph, start_node):
    # Initialize visited list to keep track of visited nodes
    visited = []
    # Initialize queue with the start_node to process nodes level by level
    queue = []
    queue.append(start_node)
    visited.append(start_node)

    # Loop to process nodes until the queue is empty
    while queue:
        # Dequeue the front node in the queue
        node = queue.pop(0)
        print(node, end=" ")  # Print the node as part of BFS traversal output

        # Visit all the child nodes (neighbors) of the current node
        for child in graph[node]:
            # Only add unvisited nodes to the queue to avoid cycles
            if child not in visited:
                queue.append(child)
                visited.append(child)

# Function to create the graph from user input
def create_graph(total_vertex):
    # Initialize an empty dictionary to store the adjacency list representation
    graph = {}
    for _ in range(total_vertex):
        # Input each vertex from the user
        vertex = input("Enter vertex: ")
        graph[vertex] = []  # Initialize an empty list for each vertex

        # Loop to add child nodes (edges) for the current vertex
        while True:
            # Input child vertex; use '-1' to stop adding children
            child = input("Enter child vertex (or -1 to stop): ")
            if child == '-1':  # Stop if input is '-1'
                break
            graph[vertex].append(child)  # Add the child to the adjacency list
    return graph  # Return the complete graph

# Main code
# Input the total number of vertices from the user
total_vertex = int(input("Enter the number of vertices: "))
graph = create_graph(total_vertex)  # Create the graph based on the input
print("Graph:", graph)  # Print the constructed graph

# Check if the graph is non-empty, then perform BFS
if graph:
    # Input starting vertex for BFS traversal
    start_vertex = input("Enter starting vertex for BFS: ")
    BFS(graph, start_vertex)  # Call BFS on the graph from the starting vertex
else:
    print("The graph is empty.")  # Print message if the graph has no vertices
