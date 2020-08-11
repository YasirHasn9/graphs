
# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Nonexisted Vertice")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bftQ(self, starting_vertex_id):
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex_id)

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                visited.add(v)
                print("visited", v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def bftS(self, starting_vertex_id):
        s = Stack()

        visited = set()
        s.push(starting_vertex_id)

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print("Visited", v)
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dftS(self, starting_vertex_id):
        s = Stack()
        visited = set()
        s.push(starting_vertex_id)

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print("dftS", v)
                for each in self.get_neighbors(v):
                    s.push(each)

    def dft_recursive(self, starting_vertex_id,  visited=None):
        print("RRRRR" , starting_vertex_id)
        if visited is None:
            visited = set()

        visited.add(starting_vertex_id)
        for each in self.vertices[starting_vertex_id]:
            if each not in visited:
                self.dft_recursive(each, visited)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('1', '0')
graph.add_edge('0', '3')
graph.add_edge('3', '0')
print(graph.vertices)
graph.dft_recursive("0")
