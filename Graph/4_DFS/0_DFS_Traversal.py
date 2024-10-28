# Function to perform DFS on a graph
def DFS(graph, start_node):
    # Initialize visited list to keep track of visited nodes
    visited = []
    # Initialize stack with the start_node to process nodes
    stack = [start_node]

    # Loop to process nodes until the stack is empty
    while stack:
        # Pop the last node from the stack (LIFO behavior)
        node = stack.pop()

        # If the node hasn't been visited, visit it
        if node not in visited:
            print(node, end=" ")  # Print the node as part of DFS traversal
            visited.append(node)

            # Add all unvisited child nodes (neighbors) to the stack
            for child in reversed(graph[node]):  # Reverse for correct order
                if child not in visited:
                    stack.append(child)


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

# Check if the graph is non-empty, then perform DFS
if graph:
    # Input starting vertex for DFS traversal
    start_vertex = input("Enter starting vertex for DFS: ")
    DFS(graph, start_vertex)  # Call DFS on the graph from the starting vertex
else:
    print("The graph is empty.")  # Print message if the graph has no vertices
