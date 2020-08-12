
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


#     def bfs(self, starting_vertex, destination):
#         q = Queue()
#         visited = set()

#         q.enqueue([starting_vertex])

#         while q.size() > 0:
#             path = q.dequeue()
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
