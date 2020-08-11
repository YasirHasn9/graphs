
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


# class Graph:
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex_id):
#         self.vertices[vertex_id] = set()

#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise IndexError("Nonexisted Vertice")

#     def get_neighbors(self, vertex_id):
#         return self.vertices[vertex_id]

#     def bft(self, starting_vertex_id):
#         q = Queue()
#         visited = set()
#         q.enqueue(starting_vertex_id)

#         while q.size() > 0:
#             v = q.dequeue()

#             if v not in visited:
#                 visited.add(v)
#                 print("visited", v)
#                 for next_vert in self.get_neighbors(v):
#                     q.enqueue(next_vert)

#     def dft(self, starting_vertex_id):
#         s = Stack()
#         visited = set()
#         s.push(starting_vertex_id)

#         while s.size():
#             v = s.pop()
#             if v not in visited:
#                 print("dft", v)
#                 visited.add(v)
#                 for each in self.get_neighbors(v):
#                     s.push(each)

#     def dft_recursive(self, node,  visited=set()):
#         '''
#         mark node as visited 
#         loop over its neighbors
#         call the function on each one of them
#         '''
#         visited.add(node)
#         print("dft_recursive", node)

#         # base case
#         if len(self.get_neighbors(node)) == 0:
#             # there is no leaf
#             return
#         for vert in self.get_neighbors(node):
#             if vert not in visited:
#                 self.dft_recursive(vert, visited)

#     def dft_recursiveBeej(self, node,  visited=None):
#         if visited is None:
#             visited = set()
#         visited.add(node)

#         for n in self.vertices[n]:
#             if n not in visited:
#                 self.dft_recursiveBeej(node, visited)

#     def bfs(self, starting_vertex, destination):
#         # 1.create an empty queue
#         q = Queue()
#         # 2.create a set so we can add the path to
#         visited = set()

#         # 3.initialize the queue with with a starting path as array
#         q.enqueue([starting_vertex])

#         # 4. loop
#         while q.size() > 0:
#             # pop off the whole item
#             path = q.dequeue()
#             # last destination in the last
#             last = path[-1]
#             if last not in visited:
#                 if last == destination:
#                     return path
#                 visited.add(last)
#                 for n in self.get_neighbors(last):
#                     n_path = list(path)
#                     n.path.append(n)
#                     q.enqueue(n_path)
    

#     def dfs_recursive(self, start,end,path=None,visited=None):
#         if visited is None:
#             visited = set()
#         if path is None:
#             path = []

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('1', '0')
# graph.add_edge('0', '3')
# graph.add_edge('3', '0')
# print(graph.vertices)
# graph.dft_recursive("0")
