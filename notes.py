'''
graphs
'''


class Graph:
    # is made of collocation of data represented by nodes
    # as sets
    def __init__(self):
        # each node will be as key in dict
        self.vertices = {}

    # we need to add nodes for the graphs (keys)

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexited node")

    '''
    since we have vertice in the graph we need to check how many neighbors 
    each vertice(node) have ?
    '''

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # create am empty queue
        q = Queue()

        # create set to store the visited nodes
        visited = set()

        # initialize: enqueue the starting node
        q.enqueue(starting_vertex_id)

        # while queue not empty
        while q.size() > 0:
            # dequeue the first node
            v = q.dequeue()
            if v not in visited:
                # then add it to visited
                # mark as visited
                visited.add(v)
                print(f"Visited {v}")
                # get all its neighbors
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
        print(q.storage)


class Queue:
    def __init__(self):
        self.storage = []

    def size(self):
        return len(self.storage)

    def enqueue(self, node):
        return self.storage.append(node)

    def dequeue(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None


g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edges("A", "B")
g.add_edges("A", "C")


g.add_edges("B", "A")
g.add_edges("B", "B")
g.add_edges("B", "C")


g.add_edges("C", "D")
g.add_edges("D", "C")
print(g.vertices)
g.bft("B")


# class Graph:
#     def __init__(self):
#         self.vertice = {}

#     def add_vertex(self, vertex_id):
#         self.vertice[vertex_id] = set()

#     def edges(self, v1, v2):
#         if v1 in self.vertice and v2 in self.vertice:
#             self.vertice[v1].add(v2)
#         else:
#             raise IndexError("Nonexited")

#     def get_neighbors(self, vertex_id):
#         return self.vertice[vertex_id]

#     def bft(self, starting_vertex_id):
#         # declear en empty q
#         q = Queue()
#         # push the visited node in the set so we can check them
#         visited = set()

#         # initialized the queue with one node
#         v = q.enqueue(starting_vertex_id)

#         # since we have something the queue then we can loop over it
#         while q.size() > 0:
#             # then dequeue the first node and add it to the visited
#             v = q.dequeue()
#             if v not in visited:
#                 visited.add(v)
#                 for next_vert in self.get_neighbors(v):
#                     q.enqueue(next_vert)
