class Vertex:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        # Initialize a vertices x edges incidence matrix
        self.inc_list = [[0 for _ in range(edges)] for _ in range(vertices)]
        self.edge_count = 0

    def add_ic_m(self, tail, head):
        if self.edge_count < self.edges:
            self.inc_list[tail][self.edge_count] = 1  # tail is the outgoing vertex
            self.inc_list[head][self.edge_count] = -1  # head is the incoming vertex
            self.edge_count += 1
        else:
            print("Error: Exceeded number of edges!")

    def display(self):
        for row in self.inc_list:
            print(row)


if __name__ == '__main__':
    # Create a graph with 4 vertices and 3 edges
    g = Vertex(4, 3)

    # Add edges (from tail to head)
    g.add_ic_m(0, 3)  # Edge 1: 0 -> 3
    g.add_ic_m(3, 2)  # Edge 2: 3 -> 2
    g.add_ic_m(2, 1)  # Edge 3: 2 -> 1

    # Display the incidence matrix
    g.display()



# ********************************************************************

class Vertex:
    def __init__(self,vertices):
        self.vertices = vertices

        self.inc_list = [[0 for  i in range(vertices)] for _ in range(vertices)]


    def add_icn_list(self,e,v):
        self.inc_list[e][v] = 1
        self.inc_list[v][e] = -1


    def display(self):
        for row in self.inc_list:
            print(row)
if __name__ == '__main__':
    g = Vertex(4)
    g.add_icn_list(0,1)
    g.add_icn_list(0,2)
    g.add_icn_list(1,3)
    g.add_icn_list(2,3)


    g.display()

