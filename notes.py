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

    def bfs(self, startVert):
        '''
        You can see that we start with a graph and the vertex 
        we will start on. The very first thing we do is go through 
        each of the vertexes in the graph and mark them with the color white.
        This means that at the outset, we mark all the verts as unvisited.
         '''
        q = Queue()
        for v in self.vertices:
            # mark them as unvisited
            self.vertices[v].update({"color": "white"})

        '''
        Next, we mark the starting vert as gray. This means we are 
        exploring the starting verts’ neighbors. We also enqueue 
        the starting vert which means it will be the first vert 
        we look at once we enter the while loop.
        '''
        self.vertices[startVert].update({"color": "gray"})
        q.enqueue(startVert)

        while q.size() > 0:
            '''
            The condition we check at the outset of each while loop is 
            if the queue is not empty. If it is not empty, we peek at 
            the first item in the queue by storing it in a variable.
            '''
            u = q.storage[0]
            for v in self.get_neighbors(u):
                '''
                Then, we loop through each of that vert’s neighbors and: - 
                We check if it is unvisited (the color white). - 
                If it is unvisited, we mark it as gray (meaning we will explore its neighbors).
                 - We enqueue the vert.
                '''
                if v.color == "white":
                    v.color = "gray"
                    q.enqueue(v)

            '''
            Next, we dequeue the current 
            vert we’ve been exploring and mark that 
            vert as black (marking it as visited).
            '''
            q.dequeue()
            u.color = "black"  # visited


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
# g.bft("B")
g.bfs("B")
