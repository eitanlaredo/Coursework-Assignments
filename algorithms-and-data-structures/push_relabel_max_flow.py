
class Edge: 
    
    def __init__(self, flow, capacity, u, v): # edges store flow, capacity, and vertice ids
        self.flow = flow
        self.capacity = capacity
        self.u = u # origin node
        self.v = v # destination node. edges go u -> v

 
class Vertex:
  
    def __init__(self, height, excess):
        self.height = height
        self.excess = excess

# To represent a flow network 
class Graph:

    def __init__(self, V): # V = number of vertices:
        
        self.V = V; 
        self.edge = []
        self.ver = []

        # initialize vertex with 0 height and excess
        # vertices are based on their indexing the array
        for _ in range(V):
            self.ver.append(Vertex(0, 0))
    
    def add_edge(self, u, v, capacity): # flow not needed, we add edges with 0 flow
        # flow is initialized with 0 for all edge 
        self.edge.append(Edge(0, capacity, u, v)) 


    def preflow(self, source):
        '''
        Preflow() 
    1) Initialize height and excess of every vertex as 0. - DONE, set up during initialization of class objects
    2) Initialize height of source vertex equal to total number of vertices in graph.
    3) Initialize flow of every edge as 0. DONE - set up during add_edge
    4) For all vertices adjacent to source s, flow and excess flow is equal to capacity initially.
        '''
        
        # Set height of source to V, numbr of vertice
        # number of vertices is length of vertices array
        self.ver[source].height = len(self.ver); 

        # iterate thru all edges, find neighbors to source and preflow them
        for edge in self.edge: 
            
        # iterate thru all edges, find neighbors to source and preflow them
            # if edge origin is source:, max its flow and set excess to this flow
            if edge.u == source:
                # Flow is equal to capacity (max out flow)
                edge.flow = edge.capacity

                # Initialize excess flow for adjacent v 
                self.ver[edge.v].excess += edge.flow

                 # Add residual edge with capacity 0
                self.edge.append(Edge(-edge.flow, 0, edge.v, source))
                

    # function to relabel vertex u 
    def relabel(self, u):
        # Start min height at infinity
        min_height = float('inf')

        # Iterate through all vertices, find min height
        for edge in self.edge:  
            if edge.u == u: # only inspect neighbors with same origin node
                
                # If flow is at capacity, no relabeling needed for u
                if (edge.flow == edge.capacity):
                    continue; 

                # find minimum height of all neighbors 
                if (self.ver[edge.v].height < min_height):
                    min_height = self.ver[edge.v].height; 

                    # updating height of u to one more than min height of all neighbors
                    self.ver[u].height = min_height + 1; 

    # Update reverse flow for flow added on ith Edge 
    def update_reverse_edges(self, i, flow):
        # i holds the index of the verse that was found in push()
        u = self.edge[i].v
        v = self.edge[i].u 

        for i in range(0, len(self.edge)): 
            if (self.edge[i].v == v and self.edge[i].u == u):
                self.edge[i].flow -= flow
                return
         # adding reverse Edge in residual graph 

        new_residual = Edge(0, flow, u, v)
        self.edge.append(new_residual)

    #  push flow from overflowing vertex u to any possible neighbors with:
    # 1. valid height and 2. available capacity
    def push(self, u):  # pushing from u to v
        
        # Traverse through all edges to find a neighbor to u that is not at capacity
        for i in range(0, len(self.edge)): 
            
            # Checks u of current edge is same as given 
            # overflowing vertex 
            if self.edge[i].u == u:
                # if flow is equal to capacity then no push 
                # is possible 
                if self.edge[i].flow == self.edge[i].capacity:
                    continue

                # Push is only possible if height of neighbor is < than height of overflowing vertex 
                if (self.ver[u].height > self.ver[self.edge[i].v].height):
                    
# Determine if we are pushing all of remaining flow - push as much as possible, up to capacity at that edge
                    # Flow to be pushed is equal to minimum of remaining flow on edge and excess flow at v. 
                    flow = min(self.edge[i].capacity - self.edge[i].flow, self.ver[u].excess)

                    # Reduce excess flow for excessed vertex 
                    self.ver[u].excess -= flow

                    # Increase excess flow for neighbor 
                    self.ver[self.edge[i].v].excess += flow; 

                    # Add residual flow (With capacity 0 and negative flow) 
                    self.edge[i].flow += flow

                    self.update_reverse_edges(i, flow)

                    return True; 

        return False;  


    # find the next vertex to discharge by iterating through all vertices
    def is_excess(self):
        
        for i in range(1, t): # range of vertices 
            if(self.ver[i].excess > 0):
                print(f"the excess of vertex {i} is {self.ver[i].excess}")
                return i

        # False if no vertex with excess - algorithm is done 
        return False
    
    def discharge(self, u):
            # discharges u, which is a vertex in excess
            # attempt to push to neighbors
            if not self.push(u):
                # if push(u) is False, u cannot push its excess, so it msut be relabeled
                self.relabel(u)
    
    # push_relabel drives the algi and get gets the max flow of graph g
    def push_relabel(self, source, t):
        # preflow the network
        self.preflow(source)

        # loop until none of the vertices are in overflow 
        while self.is_excess():
            u = self.is_excess()
            self.discharge(u)

        self.print_network()
        print(f"The max flow for this network is {self.ver[t].excess}")
        return self.ver[t].excess

    def print_network(self):
        for edge in self.edge:
            if edge.flow >= 0: # only print actual edges
                print(f"Vertex {edge.u} ---> Vertex {edge.v}. Flow: {edge.flow}/{edge.capacity}")


def generate_graph(text_file):
    # creates flow network from inut text file
    array = []
    source = float('inf') # initialize source as inf to find min value in input array
    sink = -1 # initialize sink as -1

    f = open(text_file, "r") # Open file
    
    for line in f: # iterate thru each line
        split = line.split(',')
        # Strip each line to make nested array of numbers
        if split[0] != "\n": 
            split[0] = split[0].strip()
            numbers = [int(x) for x in split]
            array.append(numbers)
    print(array)
    vertices = []

    # get number of uniqe vertices from input
    for each in array:
        if each[0] not in vertices:
            vertices.append(each[0])
        if each[1] not in vertices:
            vertices.append(each[1])

    V = len(vertices)
    g = Graph(V)
    
    for each in array: # reads input file to generate new edges on graph
        g.add_edge(each[0], each[1], each[2])

        sink = max(each[1], sink)
        min_u = min(each[0], source)
        if min_u == 1 or min_u == 0: # source may only be 1 or 0
            source = min_u
        else:
            print("Text file does not contain a valid source.\n"
                "Source must contain either a 0 or 1 vertex signifying a source")
            break
        

    return g, source, sink
    
g, s, t = generate_graph("network.txt")
g.push_relabel(s, t)



